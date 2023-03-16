import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class T4Track(models.Model):
    _name = "t4.track"
    _description = "T4 Search Track, by keyword, industry"

    _order = "search_datetime DESC"

    tag_ids = fields.Many2many(
        "res.partner.category", string="Tags", relation="t4_tag_track_rel"
    )
    industry_id = fields.Many2one("t4.industry", string="Industry")

    search_datetime = fields.Datetime(
        "Search Date", default=fields.Datetime.now, required=True, readonly=True
    )

    def create(self, vals_list):
        _logger.info(vals_list)
        super().create(vals_list)

        categories = vals_list.get("tag_ids", [])
        industry = vals_list.get("industry_id")

        self._update_count(categories, industry)

    @api.model
    def _update_count(self, _categories, _industry):
        if not _categories and not _industry:
            return False

        industry = self.env["t4.industry"]
        if _industry:
            if i := industry.browse([_industry]):
                i.write({"search_count": i.search_count + 1})

        category = self.env["res.partner.category"].browse(_categories)
        for _c in category:
            _c.write({"search_count": _c.search_count + 1})


class T4TrackContact(models.Model):
    _name = "t4.track.contact"
    _description = "T4 Search Track, record contact"

    search_datetime = fields.Datetime(
        "Search Date", default=fields.Datetime.now, required=True, readonly=True
    )


class WebsiteVisitors(models.Model):
    _name = "t4.website.visitors"
    _description = "all vistor before will render in page"
    _inherit = "t4.track"


create_date = fields.Datetime("First Connection", readonly=True)
lasst_connection_datetime = fields.Datetime(
    "Last Connection", default=fields.Datetime.now, readonly=True
)
