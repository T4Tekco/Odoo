from odoo import fields, models

class Social(models.Model):
    _name="biz.social"
    _description = "social nextwork"
    _rec_name = "social"

    social = fields.Char(string="Social")
    company_id = fields.Many2one("res.partner", string="Company")

    