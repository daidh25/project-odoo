# -*- coding: utf-8 -*-
# from odoo import http


# class Kiemtra2(http.Controller):
#     @http.route('/kiemtra2/kiemtra2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiemtra2/kiemtra2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiemtra2.listing', {
#             'root': '/kiemtra2/kiemtra2',
#             'objects': http.request.env['kiemtra2.kiemtra2'].search([]),
#         })

#     @http.route('/kiemtra2/kiemtra2/objects/<model("kiemtra2.kiemtra2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiemtra2.object', {
#             'object': obj
#         })
