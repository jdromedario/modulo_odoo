# -*- coding: utf-8 -*-
from odoo import http

# class Citasjdro(http.Controller):
#     @http.route('/citasjdro/citasjdro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citas_jdro/citas_jdro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasjdro.listing', {
#             'root': '/citas_jdro/citas_jdro',
#             'objects': http.request.env['citas_jdro.citasjdro'].search([]),
#         })

#     @http.route('/citasjdro/citasjdro/objects/<model("citas_jdro.citasjdro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citas_jdro.object', {
#             'object': obj
#         })