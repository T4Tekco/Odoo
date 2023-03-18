from odoo.addons.t4_contact_portal.controllers.main import (  # type:ignore
    BrandingPage,
    ContactPage,
)


class PrivacyBrandingPage(BrandingPage):
    def is_permission(self, contact, user):
        is_perm = super().is_permission(contact, user)
        if is_perm:
            return contact.privacy_view

        return is_perm


class PrivacyContactPage(ContactPage):
    def is_permission(self, contact, user):
        is_perm = super().is_permission(contact, user)
        if is_perm:
            return contact.privacy_view

        return is_perm
