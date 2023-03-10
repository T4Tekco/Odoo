from odoo import fields, models


class Social(models.Model):
    _name = "t4.social_network"
    _description = "social network"
    _rec_name = "social"

    social = fields.Char(string="Social")
    company_id = fields.Many2one("res.partner", string="Company")
