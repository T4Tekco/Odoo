from odoo import api, fields, models


class Attachment(models.Model):
    """T4 Contact Document"""

    _name = "t4.contact.attachment"
    _description = "T4 Document, eg: degree, certificate,..."

    name = fields.Char("Name")
    icon = fields.Char("Icon/Image")
    document_url = fields.Char("Document URL")

    contact_id = fields.Many2one("res.partner")
