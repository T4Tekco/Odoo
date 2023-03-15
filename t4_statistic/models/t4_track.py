from odoo import api, fields, models


class T4Track(models.Model):
    _name = "t4.track"
    _description = "T4 Search Track"

    _order = "search_datetime DESC"

    tag_ids = fields.Many2many(
        "res.partner.category", string="Tags", relation="t4_tag_track_rel"
    )
    industry_id = fields.Many2one("t4.industry", string="Industry")

    search_datetime = fields.Datetime(
        "Search Date", default=fields.Datetime.now, required=True, readonly=True
    )
