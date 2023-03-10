# -*- coding: utf-8 -*-
# from odoo import http


# class T4SuneditorWysiwyg(http.Controller):
#     @http.route('/t4_suneditor_wysiwyg/t4_suneditor_wysiwyg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/t4_suneditor_wysiwyg/t4_suneditor_wysiwyg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('t4_suneditor_wysiwyg.listing', {
#             'root': '/t4_suneditor_wysiwyg/t4_suneditor_wysiwyg',
#             'objects': http.request.env['t4_suneditor_wysiwyg.t4_suneditor_wysiwyg'].search([]),
#         })

#     @http.route('/t4_suneditor_wysiwyg/t4_suneditor_wysiwyg/objects/<model("t4_suneditor_wysiwyg.t4_suneditor_wysiwyg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('t4_suneditor_wysiwyg.object', {
#             'object': obj
#         })
