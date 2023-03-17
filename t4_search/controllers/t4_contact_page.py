from odoo.addons.t4_contact_portal.controllers.main import ContactPage  # type:ignore


class PrivacyContactPage(ContactPage):
    def is_permission(self, contact, user):
        is_perm = super().is_permission(contact, user)
        if is_perm:
            return contact.privacy_view

        return is_perm
