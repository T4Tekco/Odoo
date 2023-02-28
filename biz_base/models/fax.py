from odoo import models, fields


class BizFax(models.Model):
    _name = "biz.fax"
    _description = "Fax cua chi nhanh"

    fax = fields.Char(string="fax")
    company_id = fields.Many2one("res.partner", string="Company")
