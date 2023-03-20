from odoo import api, fields, models


class T4Industry(models.Model):
    _inherit = "t4.industry"

    search_portal_count = fields.Integer("Search Portal Count", default=0)  # type: ignore
