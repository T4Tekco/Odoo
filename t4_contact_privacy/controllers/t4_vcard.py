try:
    from odoo.addons.t4_vcard.controllers.download import VCardPublic  # type: ignore
except ImportError:
    VCardPublic = None


if VCardPublic is not None:

    class PrivacyVCardPublic(VCardPublic):
        def is_permission(self, contact, *args, **kwargs):
            perm = super().is_permission(contact, *args, **kwargs)
            if perm:
                return contact.privacy_download

            return perm
