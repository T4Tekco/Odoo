from odoo import fields, models


class T4Fax(models.Model):
    _name = "t4.fax"
    _description = "Fax cua chi nhanh"
    _rec_name = "fax"

    fax = fields.Char(string="Fax")
    company_id = fields.Many2one("res.partner", string="Company")
