# -*- coding: utf-8 -*-


from odoo import http
from odoo.addons.website_partner.controllers.main import WebsitePartnerPage


class BrandingPage(WebsitePartnerPage):
    def permission_for_view(self, contact, user):
        return True

    @http.route("/contacts/<int:contact_id>", type="http", auth="public", website=True)
    def partners_detail(self, contact_id, **kw):
        # contact_id = unslug(contact_id)

        if contact_id:
            contact = http.request.env["res.partner"].sudo().browse(contact_id)

            if contact:
                values = {
                    "contact": contact,
                }
                return http.request.render("t4_contact_portal.branding_page", values)

        return http.request.not_found()
