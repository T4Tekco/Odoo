# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.addons.portal.controllers import portal

_logger = logging.getLogger(__name__)


class PortalContact(http.Controller):
    FIELDS = ("name", "function", "email", "phone", "mobile")

    @http.route("/my/contact", auth="user", website=True)
    def contact_detail(self, redirect=False, **post):
        partner = http.request.env.user.partner_id

        if post and http.request.httprequest.method == "POST":
            _logger.info(post)
            _data = {key: post.get(key) for key in self.FIELDS}
            partner.sudo().write(_data)

        values = {"contact": partner}

        return http.request.render("t4_contact_portal.contact_detail_portal", values)

    @http.route("/my/branding", auth="user", website=True)
    def contact_content(self, **post):
        partner = http.request.env.user.partner_id

        if post and http.request.httprequest.method == "POST":
            _data = {"branding_content": post.get("branding_content")}
            partner.sudo().write(_data)

        values = {
            "content": partner.branding_content,
        }
        return http.request.render("t4_contact_portal.branding_portal", values)
