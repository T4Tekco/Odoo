from odoo import models, fields, api


class informationBranch(models.Models):
     _name="other.information"
     _description= "";
     phone =   fields.Many2one("res.partner","")
     fax= fields.Many2one("Fax")
     website=fields.Many2one("Website")
     email=fields.Many2one("Email")




     phone=fields.char("Phone")
class Branch (models.Models):
     
     _description= 'this is information of branch'
     _inherit="res.partner"

     phone_ids = fields.One2many('res.partner', 'phone',string="list phone")
     fax_ids= fields.One2many('res.partner','fax',string="List fax")
     webstite_ids= fields.One2many('res.partner','fax',string="Websites")
     email_ids = fields.One2many('res.partner','fax',string="List email")