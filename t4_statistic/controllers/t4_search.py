# -*- coding: utf-8 -*-
try:
    from odoo.addons.t4_search.controllers.search import T4Search  # type: ignore
except ImportError:
    T4Search = None

import logging

_logger = logging.getLogger(__name__)


if T4Search is not None:
    from odoo import http

    class T4SearchKeyword(T4Search):
        """Track after search"""

        def track_record(self, _industry=None, _keywords=None):
            category = http.request.env["res.partner.category"]
            industry = http.request.env["t4.industry"]
            track = http.request.env["t4.track"]

            categories = []
            _i = None

            if _keywords:
                for _k in _keywords:
                    if c := category.search([("name", "=", _k.strip())]):
                        categories.append(c)

            if _industry:
                _i = industry.search([("code", "=", _industry)])

            _i = _i.id if _i else None

            if not categories and not _i:
                return

            data = {"tag_ids": [c.id for c in categories], "industry_id": _i}

            track.sudo().create(data)

        def get_domain(self, **kw):
            domain = super().get_domain(**kw)  # type: ignore

            keywords = kw.get("keywords", "").split(",")
            industry = kw.get("industry", "").strip()

            self.track_record(industry, keywords)
            return domain

        def track_contact_search(self, contact_ids):
            if not contact_ids:
                return

            _logger.info(contact_ids)
            track_contact = http.request.env["t4.track.contact"]
            track_contact.sudo().create({"contact_ids": contact_ids})

        def get_recordset(self, *args, **kw):
            recordset = super().get_recordset(*args, **kw)

            self.track_contact_search([r["id"] for r in recordset])
            return recordset
