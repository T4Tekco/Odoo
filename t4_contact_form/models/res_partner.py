# -*- coding: utf-8 -*-

from odoo import api, fields, models


class T4Contact(models.Model):
    _inherit = "res.partner"

    branding_content = fields.Html(
        "Branding Content",
        sanitize=False,
        sanitize_tags=False,
        sanitize_attributes=False,
    )
