# -*- coding: utf-8 -*-

from odoo import api, fields, models


class T4ContactCategory(models.Model):
    _inherit = "res.partner.category"

    search_portal_count = fields.Integer(string="Search Count", default=0)  # type: ignore


class T4Contact(models.Model):
    _inherit = "res.partner"

    search_portal_count = fields.Integer(string="Search Count", default=0)  # type: ignore
    branding_view_count = fields.Integer(string="Branding Page View Count", default=0)  # type: ignore
    contact_view_count = fields.Integer(string="Contact Page View Count", default=0)  # type: ignore
    vcard_download_count = fields.Integer(string="vCard Download Count", default=0)  # type: ignore
