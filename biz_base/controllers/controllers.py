# -*- coding: utf-8 -*-
# from odoo import http


# class BigzBase(http.Controller):
#     @http.route('/bigz_base/bigz_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bigz_base/bigz_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bigz_base.listing', {
#             'root': '/bigz_base/bigz_base',
#             'objects': http.request.env['bigz_base.bigz_base'].search([]),
#         })

#     @http.route('/bigz_base/bigz_base/objects/<model("bigz_base.bigz_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bigz_base.object', {
#             'object': obj
#         })
