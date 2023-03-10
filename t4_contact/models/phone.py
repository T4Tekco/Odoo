from odoo import fields, models


class T4Phone(models.Model):
    _name = "t4.phone"
    _description = "Dien thoai cua chi nhanh"
    _rec_name = "phone"

    phone = fields.Char(string="Phone")
    company_id = fields.Many2one("res.partner", string="Company")
