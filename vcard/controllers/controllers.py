# -*- coding: utf-8 -*-
# from odoo import http


# class Vcard(http.Controller):
#     @http.route('/vcard/vcard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vcard/vcard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vcard.listing', {
#             'root': '/vcard/vcard',
#             'objects': http.request.env['vcard.vcard'].search([]),
#         })

#     @http.route('/vcard/vcard/objects/<model("vcard.vcard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vcard.object', {
#             'object': obj
#         })
