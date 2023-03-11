# -*- coding: utf-8 -*-


from odoo import http
from odoo.addons.website_partner.controllers.main import WebsitePartnerPage


class BrandingPage(WebsitePartnerPage):
    def permission_for_view(self, contact, user):
        return True

    def render_content(self, contact):
        if contact:
            values = {
                "contact": contact,
            }
            return http.request.render("t4_contact_portal.branding_page", values)

        return http.request.not_found()

    @http.route("/contacts/<int:contact_id>", type="http", auth="public", website=True)
    def partners_detail(self, contact_id, **kw):
        """Using Default URL"""
        if contact_id:
            contact = http.request.env["res.partner"].sudo().browse(contact_id)
            return self.render_content(contact)

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
            return self.render_content(contact)

        return http.request.not_found()
