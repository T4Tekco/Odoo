from odoo import api, fields, models


class T4Contact(models.Model):
    _inherit = "res.partner"

    privacy_search = fields.Boolean(
        "Privacy Search", default=lambda self: self._default_privacy_search()
    )
    privacy_view = fields.Boolean(
        "Privacy View", default=lambda self: self._default_privacy_view()
    )

    def _default_privacy_search(self):
        return True

    def _default_privacy_view(self):
        return True
