# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _description = "Biz Info"
    _inherit = "res.partner"

    main_industry_id = fields.Many2one("biz.industry", string="Main Industry")

    industry_ids = fields.Many2many(
        "biz.industry", relation="industry_rel", string="Sub Industries"
    )

    # ----------
    phone_ids = fields.One2many("biz.phone", "company_id", string="List Phone")
    fax_ids = fields.One2many("biz.fax", "company_id", string="List Fax")
    website_ids = fields.One2many("biz.website", "company_id", string="Websites")
    email_ids = fields.One2many("biz.email", "company_id", string="List Email")

    # --- Currency
    currency_id = fields.Many2one("res.currency")
    charter_capital = fields.Monetary("Charter Capital", "currency_id")

    # --- Hell
    owner_ids = fields.Many2many(
        "res.partner",
        relation="owner_company_rel",
        column1="company_id",
        column2="owner_id",
        string="Owners",
    )
    legal_representative_ids = fields.Many2many(
        "res.partner",
        relation="legal_company_rel",
        column1="company_id",
        column2="legal_rep_id",
        string="Legal Representatives",
    )

    identity = fields.Char("Identity ID/Business Code")

    # TODO: Add following fields:
    # Vietnam name,
    # Short name,
    # Identity ID/Business Code,
    # Owner
    # Legal Representative
    # Charter Capital
