# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _description = "Biz Info"
    _inherit = "res.partner"

    main_industry_id = fields.Many2one("biz.industry", string="Main Industry")

    industry_ids = fields.Many2many(
        "biz.industry", relation="industry_rel", string="Sub Industries"
    )
    # 1 cái list sẽ chứa nhiều danh sách
    # ví dụ: 1 list phone sẽ chứa nhiều phone
    # 1 số agrument của fields.One2many: 1. model của đối tượng 2. foreign key 3. string
    phone_ids = fields.One2many("biz.phone", "company_id", string="List Phone")
    fax_ids = fields.One2many("biz.fax", "company_id", string="List Fax")
    website_ids = fields.One2many("biz.website", "company_id", string="Websites")
    email_ids = fields.One2many("biz.email", "company_id", string="List Email")

    # 1 số agrument của fields.Many2many: 1. model chính 2. column1 là trường của bị sở hữu 3. column2 là sở hữu 4. relation 5. string
    # ví dụ ở đây: owner_id là người sở hữu công ty, company_id là côngty
    owner_ids= fields.Many2many("res.partner",column1="company_id",column2="owner_id" ,relation="owner_rel", string="Owner")

    
