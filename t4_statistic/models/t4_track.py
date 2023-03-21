import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class T4Track(models.Model):
    _name = "t4.track"
    _description = "T4 Search Track, by keyword, industry"

    _order = "search_datetime DESC"

    tag_ids = fields.Many2many(
        "res.partner.category",
        string="Tags",
        relation="t4_tag_track_rel",
    )
    industry_id = fields.Many2one("t4.industry", string="Industry")

    search_datetime = fields.Datetime(
        "Search Date", default=fields.Datetime.now, required=True, readonly=True
    )

    @api.model
    def top_keyword(self, n=5):
        keyword = self.env["res.partner.category"]
        result = keyword.search_read(
            [],
            ("name", "search_portal_count"),
            order="search_portal_count DESC",
            limit=n,
        )
        return result

    @api.model
    def top_industry_search(self, n=5):
        industry = self.env["t4.industry"]
        result = industry.search_read(
            [],
            ("name", "code", "search_portal_count"),
            order="search_portal_count DESC",
            limit=n,
        )
        return result

    @api.model
    def create(self, vals_list):
        new_record = super().create(vals_list)

        _logger.info(new_record.tag_ids)  # type: ignore
        self._update_count(new_record.tag_ids, new_record.industry_id)  # type: ignore
        return new_record

    @api.model
    def _update_count(self, _categories, _industry):
        if not _categories and not _industry:
            return False

        if _industry:
            _industry.write({"search_portal_count": _industry.search_portal_count + 1})

        for _c in _categories:
            _c.write({"search_portal_count": _c.search_portal_count + 1})

        return True


class T4TrackContact(models.Model):
    _name = "t4.track.contact"
    _description = "T4 Search Track, record contact"

    contact_ids = fields.Many2many(
        "res.partner", string="Contact", relation="t4_track_contact_rel"
    )

    search_datetime = fields.Datetime(
        "Search Date", default=fields.Datetime.now, required=True, readonly=True
    )

    @api.model
    def get_statistic(self):
        return True

    @api.model
    def top_contact_search(self, n=5):
        contact = self.env["res.partner"]
        result = contact.search_read(
            [],
            ("name", "search_portal_count"),
            order="search_portal_count DESC",
            limit=n,
        )
        return result

    @api.model
    def _default_track_type_id(self):
        TrackType = self.env["t4.track.contact.type"]
        track_type = TrackType.search([("state", "=", "search")], limit=1)
        return track_type

    @api.model
    def _group_expand_type_id(self, types, domain, order):
        return types.search([], order=order)

    track_id = fields.Many2one(
        "t4.track.contact.type",
        default=_default_track_type_id,
        group_expand="_group_expand_type_id",
    )

    track_state = fields.Selection(related="track_id.state")

    def update_contact_record(self, contacts, track_type):
        TRACK_FIELD = {
            "search": "search_portal_count",
            "branding": "branding_view_count",
            "contact": "contact_view_count",
            "download": "vcard_download_count",
        }

        for c in contacts:
            field = TRACK_FIELD[track_type]
            c.write({field: getattr(c, field) + 1})

    @api.model
    def create(self, vals_list):
        new_record = super().create(vals_list)

        _logger.info("New Track Record")

        self.update_contact_record(new_record.contact_ids, new_record.track_state)  # type: ignore

        return new_record


class T4TrackContactType(models.Model):
    _name = "t4.track.contact.type"
    _description = "Track Type for contact"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    state = fields.Selection(
        [
            ("search", "Search"),
            ("branding", "Branding Page Visit"),
            ("contact", "Contact Page Visit"),
            ("download", "vCard Download"),
        ],
    )
