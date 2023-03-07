from odoo import models, fields


class BizIndustry(models.Model):
    _name = "biz.industry"
    _description = "Nganh cua cong ty"
    _rec_name = "code"

    name = fields.Char("Industry Name")
    code = fields.Char("Industry Code", unique=True)
    company_ids = fields.One2many(
        "res.partner", string="Companies Main", inverse_name="main_industry_id", invisible = '1'
    )

    industry_ids = fields.Many2many(
        "res.partner", relation="industry_rel", string="Companies Sub"
    )
    _sql_constraints = [
        ("biz_industry_code_unique", "UNIQUE(code)", "Industry must UNIQUE")
    ]
