# -*- coding: utf-8 -*-

from odoo import http


class BrandingPage(http.Controller):
    @http.route("/contacts/<int:contact_id>", auth="public", website=True)
    def brand(self, contact_id, **kw):
        contact = (
            http.request.env["res.partner"].sudo().search([("id", "=", contact_id)])
        )
        values = {
            "contact": contact,
        }
        return http.request.render("t4_contact_form.branding", values)
