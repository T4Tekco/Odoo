from odoo import http
import logging

_logger = logging.getLogger(__name__)


class StatiticTopKeyords(http.Controller):
    #  keyword
    @http.route("/s/keyword/", auth="public", type="json", methods=["GET", "POST"])
    def statistic_keyword(self, **kw):
        return self.get_data_keyword()

    def get_data_keyword(self):
        Track = http.request.env["t4.track"]

        return Track.sudo().top_keyword()

    #  industry
    @http.route("/s/industry", auth="public", type="json", methods=["GET", "POST"])
    def statistic_industry(self, **kw):
        return self.get_data_industry()

    def get_data_industry(self):

        Track = http.request.env["t4.track"]
        return Track.sudo().top_industry_search()

    # Search
    @http.route("/s/mainpage", auth="public", type="json", methods=["GET", "POST"])
    def statistic_visitor(self, **kw):
        return self.get_data_main()

    def get_data_main(self):

        res_partner = http.request.env["res.partner"]
        mainpage = http.request.env["t4.mainpage"]
        data = dict()
        data["visit_count"] = mainpage.sudo().visit_count().get("visit_count", 0)
        data["search_portal_count"] = (
            res_partner.sudo().search_mainpage().get("search_portal_count", 0)
        )
        data["branding_view_count"] = (
            res_partner.sudo().branding_mainpage().get("branding_view_count", 0)
        )
        data["contact_view_count"] = (
            res_partner.sudo().contact_mainpage().get("contact_view_count", 0)
        )
        data["vcard_download_count"] = (
            res_partner.sudo().vcard_mainpage().get("vcard_download_count", 0)
        )
        _logger.info(data)
        return data

    #  USer
    @http.route("/s/usercontact", auth="user", type="json", methods=["GET", "POST"])
    def statistic_visitor_user(self, **kw):
        return self.get_data_user()

    def get_data_user(self):

        Track = http.request.env.user.partner_id
        data = Track.sudo().contact_statistic()
        # _logger.info(f"NH {data}")
        return data
