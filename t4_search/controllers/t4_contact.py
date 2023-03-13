# -*- coding: utf-8 -*-
from odoo import http


class T4Search(http.Controller):
    @http.route("/s/contacts/", auth="public", type="json", methods=["POST"])
    def fetch_contact(self):
        contacts = http.request.env["res.partner"].sudo().search_read([], ("name",))
        return contacts
