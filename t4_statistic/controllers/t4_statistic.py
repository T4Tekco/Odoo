from odoo import http


class StatiticTopKeyords(http.Controller):
    @http.route("/s/row/", auth="public", type="json", methods=["GET", "POST"])
    def statistic_table(self, **kw):
        return self.get_data_statistic()

    def get_data_statistic(self):
        Track = http.request.env["t4.track"]
        data = dict()
        data["top_keyword"] = Track.sudo().top_keyword()
        data["top_industry"] = Track.sudo().top_industry_search()
        return data
