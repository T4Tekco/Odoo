# -*- coding: utf-8 -*-
import base64
import logging

from odoo import http

_logger = logging.getLogger(__name__)


class VCardWiz(http.Controller):
    @http.route("/web/vcard/download", auth="public")
    def download_document(self, id, filename="contact.vcf", **kw):
        filename = "contacts.vcf"
        model = http.request.env["res.partner.t4.massvcard"]
        vcard = model.search([["id", "=", id]])

        file_content = base64.b64decode(vcard.vcf_content)

        content_type = ("Content-Type", "text/vcard")
        disposition_content = (
            "Content-Disposition",
            f"attachment; filename={filename}",
        )

        return http.request.make_response(
            file_content, [content_type, disposition_content]
        )


class VCardPublic(http.Controller):
    def is_permission(self, contact, *args, **kwargs):
        return True

    def _prepare_file(self, contact):
        if self.is_permission(contact):
            filename = f"{contact.name}-{contact.id}.vcf"
            file_content = contact.convert_to_vcard().encode()

            content_type = ("Content-Type", "text/vcard")
            disposition_content = (
                "Content-Disposition",
                f"attachment; filename={filename}",
            )

            return file_content, content_type, disposition_content

        return None

    def get_file(self, contact):
        return self._prepare_file(contact)

    @http.route("/contacts/<contact_id>/vcard", auth="public")
    def download_vcard(self, contact_id, **kw):
        contact = (
            http.request.env["res.partner"].sudo().search([("id", "=", contact_id)])
        )
        if contact:
            if data := self.get_file(contact):
                file_content, content_type, disposition_content = data
                return http.request.make_response(
                    file_content, [content_type, disposition_content]
                )

        return http.request.not_found()
