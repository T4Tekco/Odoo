from odoo import fields, models, api


class Search(models.Model):
    _name = "t4.search"
    _description = "primacy search"


primacy_search = fields.Char(string="primacy")
