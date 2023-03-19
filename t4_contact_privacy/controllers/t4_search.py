try:
    from odoo.addons.t4_search.controllers import search  # type: ignore
except ImportError:
    search = None

import logging

_logger = logging.getLogger(__name__)

if search is not None:

    class PrivacyContactFilter(search.ContactFilter):
        def initialize(self, *args, **kwargs):
            super().initialize(*args, **kwargs)
            self.domain.append(("privacy_search", "=", True))

    class PrivacyT4Search(search.T4Search):
        FILTER = PrivacyContactFilter
