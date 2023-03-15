# -*- coding: utf-8 -*-

from odoo import api, fields, models


class T4ContactCategory(models.Model):
    _inherit = "res.partner.category"

    search_count = fields.Integer(string="Search Count", default=0)  # type: ignore
