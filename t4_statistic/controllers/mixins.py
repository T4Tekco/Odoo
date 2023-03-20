from odoo import http


class TrackContactMixin:
    def track_contact(self, contact, _track_type: str):
        """
        contact: res.partner()
        _track_type: "branding" | "contact" | "download"
        """
        track = http.request.env["t4.track.contact"]
        _type = http.request.env["t4.track.contact.type"]
        _type_id = _type.sudo().search([("state", "=", _track_type)])

        track.sudo().create({"contact_ids": [contact.id], "track_id": _type_id.id})
