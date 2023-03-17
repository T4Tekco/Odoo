# -*- coding: utf-8 -*-
import functools
import logging
from abc import ABC, abstractmethod
from typing import Iterable

from odoo import http

_logger = logging.getLogger(__name__)


class BaseFilter(ABC):
    def __init__(self, value: str) -> None:
        self.domain = []
        self.initialize(value)

    @abstractmethod
    def initialize(self, value: str):
        pass

    def build_domain(self):
        return self.domain


class ContactFilter(BaseFilter):
    def initialize(self, value: str):
        self.domain.append(("name", "ilike", value))
        self.domain.append(("privacy_search", "=", True))

    def add_keyword(self, keywords: Iterable[str]):
        for keyword in keywords:
            if k := keyword.strip():
                self.domain.append(("category_id.name", "=", k))


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

    def get_recordset(self, domain, **kw):

        Contact = http.request.env["res.partner"]

        return Contact.sudo().search(domain, limit=kw.get("limit", 0))  # type:ignore

    def get_domain(self, **kw):
        query = kw.get("query", "")
        keywords = kw.get("keywords", "").split(",")

        _filter = ContactFilter(query)
        _filter.add_keyword(keywords)

        domain = _filter.build_domain()

        return domain

    def get_recordset_from_industry(self, _industry: str):
        if not _industry:
            return None

        Industry = http.request.env["t4.industry"].search([("code", "=", _industry)])

        contacts = set(Industry.company_ids + Industry.sub_company_ids)
        if contacts:
            contacts = functools.reduce(lambda a, b: a + b, contacts)

        return contacts if contacts else None

    def convert_data(self, recordset):
        fields = self._get_fields()
        return recordset.sudo().search_read([("id", "in", recordset.ids)], fields)

    def _prepare_data(self, **kw):
        _logger.info(f"query: {kw}")

        domain = self.get_domain(**kw)
        recordset = self.get_recordset(domain)

        if industry := kw.get("industry", "").strip():
            if reverse_rs := self.get_recordset_from_industry(industry):
                recordset = recordset & reverse_rs

        contacts = recordset

        contacts = self.convert_data(contacts)
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
