# -*- coding: utf-8 -*-
import logging

from odoo import http

_logger = logging.getLogger(__name__)


class T4Search(http.Controller):
    FIELDS = ("name", "website_custom_url")

    def _get_fields(self):
        return self.FIELDS

    def _get_domain(self, **kw):
        query = kw.get("query", "")

        domain = [("name", "ilike", query), ("privacy_search", "=", True)]

        return domain

    def _process_contact_url(self, contacts):
        for contact in contacts:
            if contact["website_custom_url"]:
                contact["web_url"] = f"/c/{contact['website_custom_url']}"
            else:
                contact["web_url"] = f"/contacts/{contact['id']}"

            yield contact

    def _prepare_data(self, **kw):
        domain = self._get_domain(**kw)
        fields = self._get_fields()

        contacts = (
            http.request.env["res.partner"]
            .sudo()
            .search_read(
                domain,
                fields,
                limit=kw.get("limit", 0),
            )
        )

        contacts = self._process_contact_url(contacts)

        return contacts

    @http.route("/s/contacts/", auth="public", type="json", methods=["GET", "POST"])
    def fetch_contacts(self, **kw):
        _logger.info(kw)
        _logger.info(kw.get("query"))

        return list(self._prepare_data(**kw))

    @http.route("/search/contacts", auth="public", type="http", methods=["GET"])
    def render_search(self, **kw):
        return str(list(self._prepare_data(**kw)))
