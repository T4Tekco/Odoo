from odoo import models, api


class MainPage(models.AbstractModel):
    _name = "t4.mainpage"
    _description = "Visiter Page"

    def website_track(self):
        return self.env["website.track"]

    def website_visitor(self):
        return self.env["website.visitor"]
