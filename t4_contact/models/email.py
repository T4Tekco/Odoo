from odoo import fields, models


# tạo 1 model mới
class T4Email(models.Model):
    _name = "t4.email"
    _description = "Email cua chi nhanh"
    _rec_name = "email"

    email = fields.Char(string="Email")

    company_id = fields.Many2one("res.partner", string="Company")
