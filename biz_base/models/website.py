from odoo import models,fields

class BizWebsite(models.Model):
    _name="biz.website"
    

    website=fields.Char(string="website")
    company_id = fields.Many2one('res.partner', string="Company")