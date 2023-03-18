from odoo import http
from odoo.addons.t4_contact_portal.controllers.main import (  # type: ignore
    BrandingPage,
    ContactPage,
)


class TrackBrandingPage(BrandingPage):
    pass


class TrackContactPage(ContactPage):
    pass
