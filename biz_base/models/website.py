from odoo import models, fields


class BizWebsite(models.Model):
    _name = "biz.website"
    _description = "Website cua chi nhanh"

    website = fields.Char(string="website")
    company_id = fields.Many2one("res.partner", string="Company")
