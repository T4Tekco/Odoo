from odoo import api, fields, models

from ..features.vcard_converter import VCardCreator


def _prepend_data(original, key, data: tuple):
    if data:
        original[key] = data + original[key]


def _convert_data(contact):
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

    return data


class T4Contact(models.Model):
    """For vCard features"""

    _inherit = "res.partner"

    @api.model
    def convert_to_vcard(self):
        for contact in self:
            return _convert_data(contact)

        return False
