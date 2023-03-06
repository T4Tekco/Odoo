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
                        "ORG": (contact.parent_id.name),
                        "EMAIL":[{"type": "work", "email": e.email } for e in contact.email_ids],
                        "TEL":[{"type": "work", "phone": e.phone } for e in contact.phone_ids],
                        "ADR":[contact.street,contact.city,contact.state_id.name,contact.zip,contact.country_id.name,"work"],
                        "CATEGORIES":[{"category": e.name} for e in contact.category_id],
                        "ROLE":contact.function,
                        "TZ":contact.tz,
                        "REV": contact.write_date.strftime("%Y%m%dT%H%M%SZ"),
                        "NOTE": "Test",
                        "URL":[{"type": "work", "url": e.website} for e in contact.website_ids],
                    }
                    # vCards["EMAIL"].append({"type": "main", "email": contact.email}),
                    # vCards["TEL"].append({"type": "main", "phone": contact.phone}), 
                    # vCards["URL"].append({"type": "main", "url": contact.website}),
                ).convert()
                + "\n"
            )

        _logger.info(vCards)
        return True


# TODO: Generate file, then download






