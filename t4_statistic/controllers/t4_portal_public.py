try:
    from odoo.addons.t4_contact_portal.controllers import main  # type:ignore
except ImportError:
    main = None

import logging

_logger = logging.getLogger(__name__)

if main is not None:

    class TrackBrandingPage(main.BrandingPage):
        pass

    class TrackContactPage(main.ContactPage):
        pass
