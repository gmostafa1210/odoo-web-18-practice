# -*- encoding: utf-8 -*-
###################################################################
#
#       G. Mostafa
#       Copyright (C) 2024 (https://gmostafa1210.github.io/)
#
###################################################################

from odoo import fields, models, api


class TodoList(models.Model):
    """ Model for todo list """
    _name = "todo.list"

    name = fields.Char(string="Name", required=True)
    is_done = fields.Boolean(string="Is Done", default=False)
    color = fields.Char(string="Color")
