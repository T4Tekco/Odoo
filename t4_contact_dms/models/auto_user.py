# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from typing import Any

from odoo import api, models

PREFIX_DN = "dn"
PREFIX_CN = "cn"

_logger = logging.getLogger(__name__)


class T4UserCreator(models.AbstractModel):
    _name = "t4.user.creator"
    _description = "Support BCDN"

    def res_users(self):
        return self.env["res.users"]

    def _create_user(self, login: str, contact_id: int):
        return self.res_users().create({"login": login, "partner_id": contact_id})

    def is_already_exist(self, login: str):
        return self.res_users().search_count([("login", "=", login)]) > 0

    def _generate_contact_username(self) -> Any:
        while c := datetime.now().strftime(r"%Y%m%d%H%M%S"):
            username = f"{PREFIX_CN}{c}"
            if not self.is_already_exist(username):
                return username

    def _generate_username(self, contact: Any):
        if contact.is_company:
            return f"{PREFIX_DN}{contact.identity}"
        else:
            return self._generate_contact_username()

    def _chgrp_to_portal(self, user: Any):
        """Change Security Group to Portal"""
        group_internal = self.env.ref("base.group_user")
        group_portal = self.env.ref("base.group_portal")

        # Remove from group Internal
        group_internal.write({"users": [(3, user.id)]})

        # Add to group portal
        group_portal.write({"users": [(4, user.id)]})

        return True

    def _create_bcdn_users(self, *contacts: Any):
        users = []
        for contact in contacts:
            username = self._generate_username(contact)
            user = self._create_user(username, contact.id)
            self._chgrp_to_portal(user)
            users.append(user)

        return users

    def create_bcdn_users(self, company: Any, individual: Any):
        company_user = self._create_bcdn_users(company)[0]
        individual_users = self._create_bcdn_users(*individual)

        self.send_invite_link(company_user, individual_users)

    def send_invite_link(self, company, individuals):
        Sender = self.env["t4.users.mail.bcdn"]
        Sender.mass_send_invite_mail([company] + individuals, company.email)
