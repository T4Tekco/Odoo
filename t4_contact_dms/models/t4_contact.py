# -*- coding: utf-8 -*-

import logging
from typing import Any

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

COMMON_FIELDS_MAP = {
    "name": "name",
    "identity": "identity",
    "tax_code": "vat",
    "date_of_born": "date_of_born",
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
}

INDIVIDUAL_FIELDS_MAP = {
    "sex": "sex",
    "nationality_code": "nationality_code",
    "position": "position",
}


class T4Contact(models.Model):
    _inherit = "res.partner"

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

        return {}

    def _extract_address_data(self, data):
        _fields = self._get_address_fields()

        return {}

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

    def format_data(self, data):
        self._format_data(data)

    def _create_company(self, data: Any):
        pass

    def _create_contact(self, data: Any):
        pass

    def _create_industry(self, data: Any):
        pass

    @api.model
    def bcdn(self, data: Any):
        """
        ---
        input: data
        output: response

        ---
        data:
        {
            "company_name": {
                "name": string,
                "foreign": string,
                "shortname": string
            },
            "identity": string,
            "tax_code: string,
            "date_of_born": date,
            "headquarters_address": {
                "street": string,
                "city": string,
                "zip": string,
                "state_code": string,
                "country_code": string,
                "phone": string,
                "fax": string,
                "email": string,
                "website": string
            },
            "business_sectors": {
                "main_industry_code": string,
                "sub_industries": [string, ...]
            },
            "charter_capital": float,
            "registration_office": string,
            "owners": [People, ...],
            "legal_representatives": [People, ...],
            "document_url": string
        }

        interface People
        {
            "name": string,
            "sex": "male" | "female" | "unknown",
            "day_of_birth": date,
            "national_code": string,
            "identity": string,
            "position": string,
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
            "status": "success" | "fail"
            "message": string,
        }
        """
        _logger.info(data)
        company, owners, legal_representatives = self._extract_data(data)
        _logger.info(data)
        self.format_data(company)
        _logger.info(company)

        return company
