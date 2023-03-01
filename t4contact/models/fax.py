from odoo import models, fields


class BizFax(models.Model):
    _name = "biz.fax"
    _description = "Fax cua chi nhanh"
    _rec_name = "fax"

    fax = fields.Char(string="Fax")
    company_id = fields.Many2one("res.partner", string="Company")
