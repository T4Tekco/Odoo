# -*- coding: utf-8 -*-

from odoo import api, fields, models
from collections import Counter


class T4ContactCategory(models.Model):
    _inherit = "res.partner.category"

    search_portal_count = fields.Integer(string="Search Count", default=0)  # type: ignore


class T4Contact(models.Model):
    _inherit = "res.partner"

    search_portal_count = fields.Integer(string="Search Count", default=0)  # type: ignore
    branding_view_count = fields.Integer(string="Branding Page View Count", default=0)  # type: ignore
    contact_view_count = fields.Integer(string="Contact Page View Count", default=0)  # type: ignore
    vcard_download_count = fields.Integer(string="vCard Download Count", default=0)  # type: ignore

    def contact_statistic(self):
        return {
            "search": self.search_portal_count,
            "branding": self.branding_view_count,
            "contact": self.contact_view_count,
            "vcard_down": self.vcard_download_count,
        }

    @api.model
    def search_mainpage(self):
        search = self.env["res.partner"]
        searchs = search.search([])
        result = Counter()
        for i in searchs:
            result["search_portal_count"] += i.search_portal_count
        return result

    @api.model
    def branding_mainpage(self):
        branding = self.env["res.partner"]
        brandings = branding.search([])
        result = Counter()
        for i in brandings:
            result["branding_view_count"] += i.branding_view_count

        return result

    @api.model
    def contact_mainpage(self):
        contact = self.env["res.partner"]
        contacts = contact.search([])
        result = Counter()
        for i in contacts:
            result["contact_view_count"] += i.contact_view_count
        return result

    @api.model
    def vcard_mainpage(self):
        vcard = self.env["res.partner"]
        vcards = vcard.search([])
        result = Counter()
        for i in vcards:
            result["vcard_download_count"] += i.vcard_download_count
        return result
