from odoo import models, fields


class BizEmail(models.Model):
    _name = "biz.email"
    _description = "Email cua chi nhanh"
    _rec_name = "email"

    email = fields.Char(string="Email")
    company_id = fields.Many2one("res.partner", string="Company")
