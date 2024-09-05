# -*- coding: utf-8 -*-
# from odoo import http


# class SlideAdd(http.Controller):
#     @http.route('/slide_add/slide_add', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/slide_add/slide_add/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('slide_add.listing', {
#             'root': '/slide_add/slide_add',
#             'objects': http.request.env['slide_add.slide_add'].search([]),
#         })

#     @http.route('/slide_add/slide_add/objects/<model("slide_add.slide_add"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('slide_add.object', {
#             'object': obj
#         })
