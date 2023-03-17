try:
    from odoo.addons.t4_vcard.controllers.download import VCardPublic  # type: ignore
except ImportError:
    VCardPublic = None

import logging

_logger = logging.getLogger(__name__)

if VCardPublic:
    from typing import Any

    from odoo import http

    class TrackContactDownload(VCardPublic):
        def track_download(self, contact: Any):
            track = http.request.env["t4.track.contact"]
            _type = (
                http.request.env["t4.track.contact.type"]
                .sudo()
                .search([("state", "=", "download")])
            )
            track.sudo().create({"contact_ids": [contact.id], "track_id": _type.id})

        def get_file(self, contact):
            content = super()._prepare_file(contact)
            if content:
                self.track_download(contact)

            return content

else:
    _logger.info("t4_vcard not install, ignore tracking...")
