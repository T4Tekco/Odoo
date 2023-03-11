# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate


class T4Contact(models.Model):
    _inherit = "res.partner"

    website_description = fields.Html(
        "Branding Content",
        sanitize=False,
        sanitize_tags=False,
        sanitize_attributes=False,
    )

    def _compute_website_url(self):
        super()._compute_website_url()  # type: ignore
        for partner in self:
            partner.website_url = "/contacts/%s" % partner.id  # type: ignore

    def _default_is_published(self):
        return True
