# -*- coding: utf-8 -*-


import logging

from odoo import http
from odoo.addons.website_partner.controllers.main import WebsitePartnerPage

_logger = logging.getLogger(__name__)


class BrandingPage(WebsitePartnerPage):
    def is_permission(self, contact, user):
        if user.partner_id:
            if user.partner_id.id == contact.id:
                return True

        return True

    def _prepare(self, contact, user):
        if contact and self.is_permission(contact, user):
            return self.render_content(contact)

        return http.request.not_found()

    def render_content(self, contact):
        values = {
            "contact": contact,
        }
        return http.request.render("t4_contact_portal.branding_page", values)

    @http.route("/contacts/<int:contact_id>", type="http", auth="public", website=True)
    def partners_detail(self, contact_id, **kw):
        """Using Default URL"""
        if contact_id:
            contact = http.request.env["res.partner"].sudo().browse(contact_id)
            return self._prepare(contact, http.request.env.user)

        return http.request.not_found()

    @http.route("/c/<website_custom_url>", type="http", auth="public", website=True)
    def partners_detail_2(self, website_custom_url, **kw):
        """Using Custom URL"""
        if website_custom_url:
            contact = (
                http.request.env["res.partner"]
                .sudo()
                .search([("website_custom_url", "=", website_custom_url)], limit=1)
            )
            return self._prepare(contact, http.request.env.user)

        return http.request.not_found()
