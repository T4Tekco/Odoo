# -*- coding: utf-8 -*-
import logging
from typing import Iterable

from odoo import http

_logger = logging.getLogger(__name__)


class ContactFilter:
    def __init__(self, query: str) -> None:
        self.__domain = []
        self.__domain.append(("name", "ilike", query))
        self.__domain.append(("privacy_search", "=", True))

    def add_keyword(self, keywords: Iterable[str]):
        for keyword in keywords:
            if k := keyword.strip():
                self.__domain.append(("category_id.name", "=", k))

    def add_industry(self, industry: str):
        # TODO: implement
        pass

    def build_domain(self):
        return self.__domain


class T4Search(http.Controller):
    FIELDS = ("name", "website_custom_url")

    def _get_fields(self):
        return self.FIELDS

    def _process_contact_url(self, contacts):
        for contact in contacts:
            if contact["website_custom_url"]:
                contact["web_url"] = f"/c/{contact['website_custom_url']}"
            else:
                contact["web_url"] = f"/contacts/{contact['id']}"

            yield contact

    def get_recordset(self, domain, fields, **kw):
        contacts = (
            http.request.env["res.partner"]
            .sudo()
            .search_read(
                domain,
                fields,
                limit=kw.get("limit", 0),
            )
        )

        return contacts

    def get_domain(self, **kw):
        query = kw.get("query", "")
        keywords = kw.get("keywords", "").split(",")
        industry = kw.get("industry", "").strip()

        _filter = ContactFilter(query)
        _filter.add_keyword(keywords)
        _filter.add_industry(industry)

        domain = _filter.build_domain()

        return domain

    def _prepare_data(self, **kw):
        _logger.info(f"query: {kw}")

        fields = self._get_fields()
        domain = self.get_domain(**kw)

        contacts = self.get_recordset(domain, fields, **kw)
        contacts = self._process_contact_url(contacts)

        return contacts

    @http.route("/s/contacts/", auth="public", type="json", methods=["GET", "POST"])
    def fetch_contacts(self, **kw):
        return list(self._prepare_data(**kw))

    @http.route(
        "/search/contacts", auth="public", type="http", methods=["GET"], website=True
    )
    def render_search(self, **kw):
        data = list(self._prepare_data(**kw))
        values = {"contacts": data}

        return http.request.render("t4_search.t4_contact_search_page", values)
