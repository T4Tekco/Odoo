from odoo import models, fields


class BizPhone(models.Model):
    _name = "biz.phone"
    _description = "Dien thoai cua chi nhanh"
    _rec_name = "phone"

    phone = fields.Char(string="Phone")
    company_id = fields.Many2one("res.partner", string="Company")
