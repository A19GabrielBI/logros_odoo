# -*- coding: utf-8 -*-
# from odoo import http


# class LogrosOdoo(http.Controller):
#     @http.route('/logros_odoo/logros_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/logros_odoo/logros_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('logros_odoo.listing', {
#             'root': '/logros_odoo/logros_odoo',
#             'objects': http.request.env['logros_odoo.logros_odoo'].search([]),
#         })

#     @http.route('/logros_odoo/logros_odoo/objects/<model("logros_odoo.logros_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('logros_odoo.object', {
#             'object': obj
#         })
