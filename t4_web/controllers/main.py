from odoo import http
from odoo.http import request, route


class T4Web(http.Controller):
    @http.route(["/t4tek/home"], type="http", auth="public")
    def show_playground(self):
        return request.render("t4_web.home")
    
