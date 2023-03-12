# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.addons.portal.controllers import portal

_logger = logging.getLogger(__name__)


class PortalContact(http.Controller):
    FIELDS = ("name", "function", "email", "phone", "mobile", "website_custom_url")

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
            _data = {
                "website_description": post.get("website_description"),
                "website_description_css": post.get("website_description_css"),
            }
            partner.sudo().write(_data)

        values = {
            "content": partner.website_description,
            "content_style": partner.website_description_css,
        }
        return http.request.render("t4_contact_portal.branding_portal", values)
