# -*- coding: utf-8 -*-

from typing import Any

from odoo import api, fields, models


class T4Contact(models.Model):
    _inherit = "res.partner"

    @api.model
    def parcel(self, data: Any):
        """
        data:
        {
            "company_name": {
                "name": string,
                "foreign": string,
                "shortname": string
            },
            "identity": string,
            "tax_code: string,
            "day_of_birth": date,
            "country_code": string,
            "headquarters_address": {
                "street": string,
                "city": string,
                "zip": string,
                "country": string,
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
            "owners": [people, ...],
            "legal_representatives": [people, ...]
        }

        interface people
        {
            "name": string,
            "sex": "male" | "female" | "unknown",
            "day_of_birth": date,
            "ethnicity": string,
            "identity": string,
            "position": string,
            "permanent_address": address,
            "contact_address": address,
        }

        interface address
        {
            "street": string,
            "street2": string,
            "city": string,
            "country_code": string
        }

        date format: %Y-%m-%d, eg: 2012-12-30
        """

        return {}
