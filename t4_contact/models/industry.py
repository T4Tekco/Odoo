from odoo import fields, models


class T4Industry(models.Model):
    _name = "t4.industry"
    _description = "Nganh cua cong ty"
    _rec_name = "code"

    name = fields.Char("Industry Name")
    code = fields.Char("Industry Code", required=True)
    company_ids = fields.One2many(
        "res.partner",
        string="Companies Main",
        inverse_name="main_industry_id",
        invisible="1",
    )

    sub_company_ids = fields.Many2many(
        "res.partner", relation="industry_rel", string="Companies Sub"
    )
    _sql_constraints = [
        ("t4_industry_code_unique", "UNIQUE(code)", "Industry must UNIQUE")
    ]
