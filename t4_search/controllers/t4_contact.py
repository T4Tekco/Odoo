# -*- coding: utf-8 -*-
import logging

from odoo import http

_logger = logging.getLogger(__name__)


class T4Search(http.Controller):
    @http.route("/s/contacts/", auth="public", type="json", methods=["GET"])
    def fetch_contact(self):
        _logger.info(http.request.env.user)
        contacts = http.request.env["res.partner"].sudo().search_read([], ("name",))
        return contacts
