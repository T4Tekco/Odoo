# -*- coding: utf-8 -*-

import logging
from typing import Any

from odoo import api, models

_logger = logging.getLogger(__name__)

COMMON_FIELDS_MAP = {
    "name": "name",
    "identity": "identity",
    "tax_code": "vat",
    "date_of_birth": "date_of_birth",
    "charter_capital": "charter_capital",
}

ADDRESS_FIELDS_MAP = {
    "street": "street",
    "street2": "street2",
    "city": "city",
    "zip": "zip",
    "state_code": "state_id",
    "country_code": "country_id",
}

COMPANY_FIELDS_MAP = {
    "foreign_name": "foreign_name",
    "short_name": "short_name",
    "phone": "phone",
    "email": "email",
    "website": "website",
    "registration_office": "registration_office",
    "fax": "fax_ids",
    "main_industry_code": "main_industry_id",
    "sub_industries": "industry_ids",
    "document_url": "document_url",
}

INDIVIDUAL_FIELDS_MAP = {
    "sex": "sex",
    "nationality_code": "nationality_id",
    "position": "function",
}

RESPONSE = {
    0: {"status": "success", "message": ""},
    1: {"status": "failure", "message": "Format error"},
    2: {"status": "failure", "message": "Already exists"},
}

MANDATORY = ("name", "identity")


class T4ContactBCDN(models.AbstractModel):
    _name = "t4.contact.bcdn"
    _description = "BCDN functions"

    def res_partner(self):
        return self.env["res.partner"]

    def _pre_check(self, data):
        for field in MANDATORY:
            if field not in data:
                return False

        return True

    def pre_check(self, *args):
        for data in args:
            if not self._pre_check(data):
                return False

        return True

    def _get_company_fields(self):
        return COMMON_FIELDS_MAP | ADDRESS_FIELDS_MAP | COMPANY_FIELDS_MAP

    def _get_individual_fields(self):
        return COMMON_FIELDS_MAP | ADDRESS_FIELDS_MAP | INDIVIDUAL_FIELDS_MAP

    def _get_address_fields(self):
        return ADDRESS_FIELDS_MAP

    def _extract_company_data(self, data):
        _fields = self._get_company_fields()
        return {_fields[k]: v for k, v in data.items()}

    def _extract_individual_data(self, data):
        _fields = self._get_individual_fields()
        data = dict(data)
        address = {}
        contact_address = {}
        if "permanent_address" in data:
            address = self._extract_address_data(data.pop("permanent_address"))
        if "contact_address" in data:
            contact_address = self._extract_address_data(data.pop("contact_address"))

        individual = {_fields[k]: v for k, v in data.items()}
        individual |= address
        individual["contact_address"] = contact_address
        return individual

    def _extract_address_data(self, data):
        _fields = self._get_address_fields()
        return {_fields[k]: v for k, v in data.items()}

    def _extract_data(self, data: Any):
        company_data = self._extract_company_data(data["company"])

        owners = [self._extract_individual_data(p) for p in data["owners"]]
        legal_representatives = [
            self._extract_individual_data(p) for p in data["legal_representatives"]
        ]

        return company_data, owners, legal_representatives

    def _get_country_id(self, country_code):
        return self.env["res.country"].search([("code", "=", country_code)], limit=1).id

    def _get_state_id(self, state_code):
        return (
            self.env["res.country.state"]
            .search([("code", "=", state_code)], limit=1)
            .id
        )

    def _format_data(self, data: Any):
        """
        Convert 'code' -> 'id'
        """
        if "country_id" in data:
            data["country_id"] = self._get_country_id(data["country_id"])

        if "state_id" in data:
            data["state_id"] = self._get_state_id(data["state_id"])

        if "nationality_id" in data:
            data["nationality_id"] = self._get_country_id(data["nationality_id"])

        if "main_industry_id" in data:
            data["main_industry_id"] = self._create_or_get_industry(
                data["main_industry_id"]
            )

        if "industry_ids" in data:
            data["industry_ids"] = [
                self._create_or_get_industry(code) for code in data["industry_ids"]
            ]

        if "fax_ids" in data:
            if data["fax_ids"]:
                data["fax_ids"] = [self._create_fax(data["fax_ids"])]
            else:
                data.pop("fax_ids")

        return data

    def format_data(self, data):
        return self._format_data(data)

    def format_contacts_data(self, contacts):
        result = []
        for o in contacts:
            o = self.format_data(o)
            if "contact_address" in o:
                o["contact_address"] = self.format_data(o["contact_address"])
            result.append(o)

        return result

    def _create_company(self, data: Any, owners, legals):
        data["is_company"] = True
        data["owner_ids"] = owners
        data["legal_representative_ids"] = legals
        data["child_ids"] = list(set(owners + legals))

        if "document_url" in data:
            if doc_url := data.pop("document_url"):
                attachment_id = self._create_document(doc_url)
                data["attachment_ids"] = [attachment_id]

        return self.res_partner().create(data)

    def _create_document(self, document_url: str) -> int:
        Attachment = self.env["t4.contact.attachment"]

        return Attachment.create(
            {
                "name": "Bo Cao Doanh Nghiep",
                "icon": "/t4_contact_dms/static/src/img/download-pdf.png",
                "document_url": document_url,
            }
        ).id

    def _create_fax(self, fax: str):
        Fax = self.env["t4.fax"]

        return Fax.create({"fax": fax}).id

    def _create_contact(self, data: Any):
        contact_address = None
        if "contact_address" in data:
            contact_address = data.pop("contact_address")
            contact_address["type"] = "other"

        contact = self.res_partner().create(data)

        if contact_address:
            contact_address["parent_id"] = contact.id  # type: ignore
            self.res_partner().create(contact_address)

        return contact

    def create_contact(self, data: Any):
        return self._create_contact(data)

    def _process_contacts(self, owners, legal_representatives):
        owner_table = {p["identity"]: p for p in owners}
        legal_table = {p["identity"]: p for p in legal_representatives}
        owner_ids = []
        legal_ids = []

        for k, v in owner_table.items():
            if k in legal_table:
                contact = self.create_contact(v | legal_table[k])
                legal_ids.append(contact.id)
                legal_table.pop(k)
            else:
                contact = self.create_contact(v)

        for k, v in legal_table.items():
            legal_ids.append(self.create_contact(v).id)

        return owner_ids, legal_ids

    def _create_or_get_industry(self, industry_code: Any):
        Industry = self.env["t4.industry"]
        i = Industry.search([("code", "=", industry_code)], limit=1)
        _id = i.id if i else Industry.create({"code": industry_code}).id
        return _id

    @api.model
    def bcdn(self, data: Any):
        """
        ---
        input: data
        output: response

        ---
        data:
        {
            "company": {
                "name": string,
                "foreign_name": string,
                "short_name": string,
                "identity": string,
                "tax_code": string,
                "date_of_birth": date,
                "street": string,
                "city": string,
                "zip": string,
                "state_code": string,
                "country_code": string,
                "phone": string,
                "fax": string,
                "email": string,
                "website": string,
                "main_industry_code": string,
                "sub_industries": [string, ...],
                "charter_capital": float,
                "registration_office": string,
                "document_url": string,
            }
            "owners": [People, ...],
            "legal_representatives": [People, ...]
        }

        interface People
        {
            "name": string,
            "position": string,
            "sex": "male" | "female" | "unknown",
            "date_of_birth": date,
            "nationality_code": string,
            "identity": string,
            "permanent_address": Address,
            "contact_address": Address,
        }

        interface Address
        {
            "street": string,
            "street2": string,
            "city": string,
            "state_code": string,
            "zip": string,
            "country_code": string
        }

        date format: %Y-%m-%d, eg: 2012-12-30

        ---
        response
        {
            "status": "success" | "failure",
            "message": string
        }
        """
        _response_code = 0

        try:
            company, owners, legal_representatives = self._extract_data(data)
        except KeyError:
            return RESPONSE[1]

        # ------------------------------------
        if not self.pre_check(company, *owners, *legal_representatives):
            return RESPONSE[1]

        # ------------------------------------
        if self.res_partner().search([("identity", "=", company["identity"])]):
            _response_code = 2
        else:
            company = self.format_data(company)
            owners = self.format_contacts_data(owners)
            legal_representatives = self.format_contacts_data(legal_representatives)

            owner_ids, legal_ids = self._process_contacts(owners, legal_representatives)

            company = self._create_company(company, owner_ids, legal_ids)

            # -------

            input_for_auto_users = [company] + [
                c for c in self.res_partner().search([("id", "in", legal_ids)])
            ]

            self.env["t4.user.creator"].sudo().create_bcdn_users(input_for_auto_users)

            # --------

            _logger.info(company)
            _logger.info(owners)
            _logger.info(legal_representatives)

        # -------------------------------------

        return RESPONSE[_response_code]
