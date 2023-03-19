from odoo import api, fields, models


class T4Contact(models.Model):
    """For search feature, not privacy"""

    _inherit = "res.partner"

    # priority = fields.Selection(
    #     [
    #         ("0", "Normal"),
    #         ("1", "Favorite"),
    #     ],
    #     default="0",
    #     string="Favorite",
    # )
