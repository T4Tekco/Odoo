# -*- coding: utf-8 -*-


import logging

from odoo import http
from odoo.addons.website_partner.controllers.main import WebsitePartnerPage

_logger = logging.getLogger(__name__)


class ContactRenderMixin:
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

    def _prepare(self, contact, user):
        if contact and self.is_permission(contact, user):
            data = {
                "contact": contact,
            }
            return data

        return None

    def prepare(self, contact, user):
        return self._prepare(contact, user)

    def render(self, user, template, _data):
        data = self.prepare(_data, user)
        if data:
            return http.request.render(template, data)

        return http.request.not_found()


class BrandingPage(ContactRenderMixin, WebsitePartnerPage):
    @http.route("/branding/<int:contact_id>", type="http", auth="public", website=True)
    def partners_detail(self, contact_id, **kw):
        """
        Branding Page\n
        Using Default URL
        """
        if contact_id:
            contact = self._get_contact_by_id(contact_id)
            return self.render(
                http.request.env.user, "t4_contact_portal.branding_page", contact
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
            return self.render(
                http.request.env.user, "t4_contact_portal.branding_page", contact
            )

        return http.request.not_found()


class ContactPage(ContactRenderMixin, http.Controller):
    @http.route("/contacts/<int:contact_id>", type="http", auth="public", website=True)
    def contact_detail(self, contact_id, **kw):
        """
        Contact Page
        """
        if contact_id:
            contact = self._get_contact_by_id(contact_id)
            return self.render(
                http.request.env.user, "t4_contact_portal.contact_page", contact
            )

        return http.request.not_found()
