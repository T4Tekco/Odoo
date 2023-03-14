# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class t4_statistic(models.Model):
#     _name = 't4_statistic.t4_statistic'
#     _description = 't4_statistic.t4_statistic'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
