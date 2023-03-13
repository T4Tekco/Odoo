# -*- coding: utf-8 -*-
# from odoo import http


# class T4Search(http.Controller):
#     @http.route('/t4_search/t4_search', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/t4_search/t4_search/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('t4_search.listing', {
#             'root': '/t4_search/t4_search',
#             'objects': http.request.env['t4_search.t4_search'].search([]),
#         })

#     @http.route('/t4_search/t4_search/objects/<model("t4_search.t4_search"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('t4_search.object', {
#             'object': obj
#         })
