from odoo import models, fields


class BizWebsite(models.Model):
    _name = "biz.website"
    _description = "Website cua chi nhanh"
    _rec_name = "website"

    website = fields.Char(string="Website")
    company_id = fields.Many2one("res.partner", string="Company")
