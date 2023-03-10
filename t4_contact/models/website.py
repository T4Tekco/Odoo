from odoo import fields, models


class T4Website(models.Model):
    _name = "t4.website"
    _description = "Website cua chi nhanh"
    _rec_name = "website"

    website = fields.Char(string="Website")
    company_id = fields.Many2one("res.partner", string="Company")
