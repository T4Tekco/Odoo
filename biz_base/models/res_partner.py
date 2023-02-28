# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _description = "Biz Info"
    _inherit = "res.partner"
