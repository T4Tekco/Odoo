# -*- coding: utf-8 -*-


import logging

from odoo import http
from odoo.addons.website_partner.controllers.main import WebsitePartnerPage

_logger = logging.getLogger(__name__)


class ContactPage(WebsitePartnerPage):
    def is_permission(self, contact, user):
        if user.partner_id:
            if user.partner_id.id == contact.id:
                return True

        return True

    def _get_contact_by_id(self, contact_id):
        return (
            http.request.env["res.partner"]
            .sudo()
            .search([("id", "=", contact_id)], limit=1)
        )

    def _prepare(self, contact, user, template):
        if contact and self.is_permission(contact, user):
            return self.render_content(contact, template)

        return http.request.not_found()

    def render_content(self, contact, template):
        values = {
            "contact": contact,
        }
        return http.request.render(template, values)

    @http.route("/branding/<int:contact_id>", type="http", auth="public", website=True)
    def partners_detail(self, contact_id, **kw):
        """
        Branding Page\n
        Using Default URL
        """
        if contact_id:
            contact = self._get_contact_by_id(contact_id)
            return self._prepare(
                contact, http.request.env.user, "t4_contact_portal.branding_page"
            )

        return http.request.not_found()

    @http.route("/b/<website_custom_url>", type="http", auth="public", website=True)
    def partners_detail_2(self, website_custom_url, **kw):
        """
        Branding Page\n
        Using Custom URL"""
        if website_custom_url:
            contact = (
                http.request.env["res.partner"]
                .sudo()
                .search([("website_custom_url", "=", website_custom_url)], limit=1)
            )
            return self._prepare(
                contact, http.request.env.user, "t4_contact_portal.branding_page"
            )

        return http.request.not_found()

    @http.route("/contacts/<int:contact_id>", type="http", auth="public", website=True)
    def contact_detail(self, contact_id, **kw):
        """
        Contact Page
        """
        if contact_id:
            contact = self._get_contact_by_id(contact_id)
            return self._prepare(
                contact, http.request.env.user, "t4_contact_portal.contact_page"
            )

        return http.request.not_found()
