# -*- coding: utf-8 -*-

import logging
from typing import Any

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class T4Contact(models.Model):
    _inherit = "res.partner"

    @api.model
    def bcdn(self, data: Any):
        return self.env["t4.contact.bcdn"].bcdn(data)
