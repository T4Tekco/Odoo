from odoo import api, models, fields, exceptions
from ..features.vcard_converter import VCardCreator

import logging

_logger = logging.getLogger(__name__)


class CheckoutMassMessage(models.TransientModel):
    _name = "res.partner.t4.massvcard"
    _description = "Send message to Borrowers"

    t4contact_ids = fields.Many2many(
        "res.partner", relation="t4contact_mm_rel_wz", string="Checkouts"
    )

    @api.model
    def default_get(self, fields_list):
        defaults_dict = super().default_get(fields_list)
        t4contact_ids = self.env.context["active_ids"]
        defaults_dict["t4contact_ids"] = [(6, 0, t4contact_ids)]
        return defaults_dict

    # self.
    def button_export_vcard(self):
        self.ensure_one()
        if not self.t4contact_ids:
            raise exceptions.UserError("No Contacts were select.")

        vCards = ""

        for contact in self.t4contact_ids:
            vCards += (
                VCardCreator(
                    {
                        "version": "4.0",
                        "N": (contact.name,),
                        "FN": contact.name,
                    }
                ).convert()
                + "\n"
            )

        _logger.info(vCards)
        return True


# TODO: Generate file, then download
