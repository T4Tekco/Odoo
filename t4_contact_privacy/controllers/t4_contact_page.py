try:
    from odoo.addons.t4_contact_portal.controllers import main  # type:ignore
except ImportError:
    main = None

import logging

_logger = logging.getLogger(__name__)

if main is not None:

    class PrivacyBrandingPage(main.BrandingPage):
        def is_permission(self, contact, user):
            is_perm = super().is_permission(contact, user)
            if is_perm:
                return contact.privacy_view

            return is_perm

    class PrivacyContactPage(main.ContactPage):
        def is_permission(self, contact, user):
            is_perm = super().is_permission(contact, user)
            if is_perm:
                return contact.privacy_view

            return is_perm
