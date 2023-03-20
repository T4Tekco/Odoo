try:
    from odoo.addons.t4_contact_portal.controllers import main  # type:ignore
except ImportError:
    main = None

import logging

_logger = logging.getLogger(__name__)

if main is not None:

    from .mixins import TrackContactMixin

    class TrackBrandingPage(TrackContactMixin, main.BrandingPage):
        def prepare(self, contact, user):
            data = super().prepare(contact, user)
            if data:
                self.track_contact(contact, "branding")

            return data

    class TrackContactPage(TrackContactMixin, main.ContactPage):
        def prepare(self, contact, user):
            data = super().prepare(contact, user)
            if data:
                self.track_contact(contact, "contact")

            return data
