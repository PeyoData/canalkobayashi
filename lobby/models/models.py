# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lobby(models.Model):
    _name = 'lobby.lobby'
    _description = 'lobby.lobby'

    name = fields.Char()
    description = fields.Text()
