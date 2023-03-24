# -*- coding: utf-8 -*-

import logging
from typing import Any

from odoo import api, models

_logger = logging.getLogger(__name__)


class T4UserCreator(models.AbstractModel):
    _name = "t4.user.creator"
    _description = "Support BCDN"

    def res_users(self):
        return self.env["res.users"]
