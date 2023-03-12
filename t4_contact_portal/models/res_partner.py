# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slugify
from odoo.tools.translate import html_translate

_logger = logging.getLogger(__name__)


class T4Contact(models.Model):
    _inherit = "res.partner"

    website_description = fields.Html(
        "Branding Content",
        sanitize=False,
        sanitize_tags=False,
        sanitize_attributes=False,
    )

    website_description_css = fields.Char("Web Style")

    # Branding Page custom URL
    website_custom_url = fields.Char("Custom URL")

    _sql_constraints = [
        ("t4_website_custom_url", "UNIQUE(website_custom_url)", "Already exists")
    ]

    def write(self, vals):
        if s := vals.get("website_custom_url"):
            if s := str(s).strip():
                vals["website_custom_url"] = slugify(s)
        return super().write(vals)

    def _compute_website_url(self):
        super()._compute_website_url()  # type: ignore
        for partner in self:
            partner.website_url = "/contacts/%s" % partner.id  # type: ignore

    def _default_is_published(self):
        return True
