# -*- coding: utf-8 -*-
from openerp import http

# class Mymodules/redond(http.Controller):
#     @http.route('/mymodules/redond/mymodules/redond/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mymodules/redond/mymodules/redond/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mymodules/redond.listing', {
#             'root': '/mymodules/redond/mymodules/redond',
#             'objects': http.request.env['mymodules/redond.mymodules/redond'].search([]),
#         })

#     @http.route('/mymodules/redond/mymodules/redond/objects/<model("mymodules/redond.mymodules/redond"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mymodules/redond.object', {
#             'object': obj
#         })