from odoo import api, fields, models


class Attachment(models.Model):
    """T4 Contact Document: set default icon url"""

    _inherit = "t4.contact.attachment"

    name = fields.Char("Name")
    icon = fields.Char(default=lambda self: self.default_icon_url())

    def default_icon_url(self):
        return "/t4_contact_dms/static/src/img/attach-paperclip-symbol.png"
