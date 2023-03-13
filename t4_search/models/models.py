# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class t4_search(models.Model):
#     _name = 't4_search.t4_search'
#     _description = 't4_search.t4_search'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
