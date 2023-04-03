from odoo import models, api
from collections import Counter


class MainPage(models.AbstractModel):
    _name = "t4.mainpage"
    _description = "Visiter Page"

    def website_track(self):
        return self.env["website.track"]

    def website_visitor(self):
        return self.env["website.visitor"]

    @api.model
    def visit_count(self):
        visit = self.env["website.visitor"]
        visits = visit.search([])
        result = Counter()
        for i in visits:
            result["visit_count"] += i.visit_count
        return result
