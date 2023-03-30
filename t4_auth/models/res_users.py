import logging
from datetime import datetime, timedelta

from odoo import _, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


def now(**kwargs):
    return datetime.now() + timedelta(**kwargs)


class ResUserMail(models.AbstractModel):
    """support bcdn"""

    _name = "t4.users.mail.bcdn"

    def res_users(self):
        return self.env["res.users"]

    def __execute_reset_password_mail(self, user, company_mail: str):
        """copy-paste code"""
        expiration = False
        user.mapped("partner_id").signup_prepare(
            signup_type="reset", expiration=expiration
        )

        template = False

        template = self.env.ref(
            "auth_signup.set_password_email", raise_if_not_found=False
        )

        assert template._name == "mail.template"

        email_values = {
            "email_cc": False,
            "auto_delete": True,
            "message_type": "user_notification",
            "recipient_ids": [],
            "partner_ids": [],
            "scheduled_date": False,
        }

        if user and company_mail:
            email_values["email_to"] = company_mail

            with self.env.cr.savepoint():

                template.send_mail(
                    user.id,
                    force_send=True,
                    raise_exception=True,
                    email_values=email_values,
                )
            _logger.info(
                "Password reset email sent for user <%s> to <%s>",
                user.login,
                user.email,
            )

    def _execute_set_password_mail(self, user, company_mail):
        return self.__execute_reset_password_mail(user, company_mail)

    def mass_send_invite_mail(self, users, company_mail):
        for user in users:
            self._execute_set_password_mail(user, company_mail)

        return True
