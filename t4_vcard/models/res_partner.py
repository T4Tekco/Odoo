from odoo import fields, models, api
from ..features.vcard_converter import VCardCreator


class T4Contact(models.Model):
    """For vCard features"""

    _inherit = "res.partner"

    # @api.model
    # def button_to_vcard(self):
    #     """Implement"""
    #     name = ""
    #     full_name = ""

    #     for contact in self:
    #         name = contact.name  # type: ignore
    #         full_name = contact.name  # type: ignore

    #     data = {
    #         "version": "4.0",
    #         "N": (name,),
    #         "FN": full_name,
    #     }

    #     return {"vcard": VCardCreator(data).convert()}
