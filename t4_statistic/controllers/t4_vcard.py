try:
    from odoo.addons.t4_vcard.controllers.download import VCardPublic  # type: ignore
except ImportError:
    VCardPublic = None

import logging

_logger = logging.getLogger(__name__)

if VCardPublic is not None:
    from .mixins import TrackContactMixin

    class TrackContactDownload(TrackContactMixin, VCardPublic):
        def get_file(self, contact):
            content = super().get_file(contact)
            if content:
                self.track_contact(contact, "download")

            return content
