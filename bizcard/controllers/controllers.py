# -*- coding: utf-8 -*-
# from odoo import http


# class Bizcard(http.Controller):
#     @http.route('/bizcard/bizcard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bizcard/bizcard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bizcard.listing', {
#             'root': '/bizcard/bizcard',
#             'objects': http.request.env['bizcard.bizcard'].search([]),
#         })

#     @http.route('/bizcard/bizcard/objects/<model("bizcard.bizcard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bizcard.object', {
#             'object': obj
#         })
