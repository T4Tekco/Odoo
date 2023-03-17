import base64
import logging
from typing import Any

from odoo import api, exceptions, fields, models

from ..features.vcard_converter import VCardCreator

_logger = logging.getLogger(__name__)


class CheckoutMassMessage(models.TransientModel):
    _name = "res.partner.t4.massvcard"
    _description = "Send message to Borrowers"

    t4contact_ids = fields.Many2many(
        "res.partner", relation="t4contact_mm_rel_wz", string="Checkouts"
    )
    vcf_content = fields.Binary("vCard file", readonly=True)

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
            data = contact.convert_to_vcard()  # type: ignore

            _logger.debug(data)

            vCards += VCardCreator(data).convert() + "\n\n"

        self.vcf_content = base64.b64encode(str.encode(vCards))

        return {
            "type": "ir.actions.act_url",
            "url": f"/web/vcard/download?model=res.partner.t4.massvcard&id={self.id}",  # type: ignore
            "target": "self",
        }
