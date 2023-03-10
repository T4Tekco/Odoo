import base64
import logging
from typing import Any

from odoo import api, exceptions, fields, models

from ..features.vcard_converter import VCardCreator

_logger = logging.getLogger(__name__)


def _prepend_data(original, key, data: tuple):
    if data:
        original[key] = data + original[key]


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
            contact: Any

            data = {
                "version": "4.0",
                "N": (contact.name,),
                "FN": contact.name,
                "ORG": (contact.parent_id.name,),
                "EMAIL": tuple(("work", e.email) for e in contact.email_ids),
                "TEL": tuple((("work",), e.phone) for e in contact.phone_ids),
                "ADR": (
                    (
                        contact.street,
                        contact.city,
                        contact.state_id.name,
                        contact.zip,
                        contact.country_id.name,
                        "work",
                    ),
                ),
                "CATEGORIES": tuple(e.name for e in contact.category_id),
                "ROLE": contact.title.name,
                "TITLE": contact.function,
                "TZ": contact.tz,
                "REV": contact.write_date.strftime("%Y%m%dT%H%M%SZ"),
                "NOTE": "",
                "URL": tuple(("work", e.website) for e in contact.website_ids),
                "PHOTO": contact.image_1920,
            }

            _prepend_data(data, "EMAIL", (("home", contact.email),))
            _prepend_data(data, "TEL", ((("home",), contact.phone),))
            _prepend_data(data, "URL", (("home", contact.website),))

            _logger.debug(data)

            vCards += VCardCreator(data).convert() + "\n\n"

        self.vcf_content = base64.b64encode(str.encode(vCards))

        return {
            "type": "ir.actions.act_url",
            "url": f"/web/vcard/download?model=res.partner.t4.massvcard&id={self.id}",  # type: ignore
            "target": "self",
        }
