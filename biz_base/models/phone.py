from odoo import models,fields

class BizPhone(models.Model):
    _name="biz.phone"
    

    phone=fields.Char(string="phone")
    company_id = fields.Many2one('res.partner', string="Company")