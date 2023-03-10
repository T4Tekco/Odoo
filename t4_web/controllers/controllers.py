# -*- coding: utf-8 -*-
# from odoo import http


# class BizcardWeb(http.Controller):
#     @http.route('/bizcard_web/bizcard_web', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bizcard_web/bizcard_web/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bizcard_web.listing', {
#             'root': '/bizcard_web/bizcard_web',
#             'objects': http.request.env['bizcard_web.bizcard_web'].search([]),
#         })

#     @http.route('/bizcard_web/bizcard_web/objects/<model("bizcard_web.bizcard_web"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bizcard_web.object', {
#             'object': obj
#         })
