from odoo import fields, models, api


class Search(models.Model):
    _name = "biz.search"
    _description = "primacy search"


primacy_search = fields.Char(string="primacy")
