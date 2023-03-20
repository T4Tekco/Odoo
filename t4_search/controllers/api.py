from odoo import http


class SearchFilterHelper(http.Controller):
    @http.route("/f/keywords", auth="public", type="json", methods=["GET", "POST"])
    def fetch_tags(self, **kw):
        Tag = http.request.env["res.partner.category"]
        fields = ("name",)

        return Tag.search_read([], fields)

    @http.route("/f/industries", auth="public", type="json", methods=["GET", "POST"])
    def fetch_industries(self, **kw):
        Industry = http.request.env["t4.industry"]
        fields = ("name", "code")

        return Industry.search_read([], fields)
