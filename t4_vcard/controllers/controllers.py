# -*- coding: utf-8 -*-
from odoo import http
import base64


class Vcard(http.Controller):
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
