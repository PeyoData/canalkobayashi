# -*- coding: utf-8 -*-
# from odoo import http


# class Lobby(http.Controller):
#     @http.route('/lobby/lobby/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lobby/lobby/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lobby.listing', {
#             'root': '/lobby/lobby',
#             'objects': http.request.env['lobby.lobby'].search([]),
#         })

#     @http.route('/lobby/lobby/objects/<model("lobby.lobby"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lobby.object', {
#             'object': obj
#         })
