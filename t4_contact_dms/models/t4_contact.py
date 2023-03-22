# -*- coding: utf-8 -*-

import logging
from typing import Any

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class T4Contact(models.Model):
    _inherit = "res.partner"

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
                "state_code", string,
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
            "ethnicity": string,
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

        return True
