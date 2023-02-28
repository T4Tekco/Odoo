from odoo import models,fields

class BizEmail(models.Model):
    _name="biz.email"
    

    email=fields.Char(string="Email")
    company_id = fields.Many2one('res.partner', string="Company")