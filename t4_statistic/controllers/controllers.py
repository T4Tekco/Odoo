# -*- coding: utf-8 -*-
# from odoo import http


# class T4Statistic(http.Controller):
#     @http.route('/t4_statistic/t4_statistic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/t4_statistic/t4_statistic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('t4_statistic.listing', {
#             'root': '/t4_statistic/t4_statistic',
#             'objects': http.request.env['t4_statistic.t4_statistic'].search([]),
#         })

#     @http.route('/t4_statistic/t4_statistic/objects/<model("t4_statistic.t4_statistic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('t4_statistic.object', {
#             'object': obj
#         })
