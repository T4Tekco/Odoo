# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _description = "Biz Info"
    _inherit = "res.partner"

    main_industry_id = fields.Many2one(
        "biz.industry", required=True, string="Main Industry"
    )

    industry_ids = fields.Many2many(
        "biz.industry", relation="industry_rel", string="Sub Industries"
    )
