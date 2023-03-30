# -*- coding: utf-8 -*-
import logging

import werkzeug  # type: ignore
from werkzeug.urls import url_encode  # type: ignore

from odoo import _, http
from odoo.addons.auth_signup.controllers import main
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)

# TODO: Sửa URL của invite mail, đọc mã nguồn của nó, vớ va vớ vẩn.


class T4Signup(main.AuthSignupHome):
    @http.route()
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()

        _logger.info(f"T4: Qcontext {qcontext}")

        if not qcontext.get("token") and not qcontext.get("signup_enabled"):
            raise werkzeug.exceptions.NotFound()

        if "error" not in qcontext and request.httprequest.method == "POST":
            try:
                if e := qcontext.get("email", "").strip():
                    data = {
                        "name": qcontext.get("name", ""),
                        "email": e,
                    }

                    partner = http.request.env["res.partner"].sudo().create(data)
                    qcontext["partner_id"] = partner.id

                self.do_signup(qcontext)
                # Send an account creation confirmation email
                if qcontext.get("token"):
                    User = request.env["res.users"]
                    user_sudo = User.sudo().search(
                        User._get_login_domain(qcontext.get("login")),
                        order=User._get_login_order(),
                        limit=1,
                    )
                    template = request.env.ref(
                        "auth_signup.mail_template_user_signup_account_created",
                        raise_if_not_found=False,
                    )
                    if user_sudo and template:
                        template.sudo().send_mail(user_sudo.id, force_send=True)
                return self.web_login(*args, **kw)
            except UserError as e:
                qcontext["error"] = e.args[0]
            except (SignupError, AssertionError) as e:
                if (
                    request.env["res.users"]
                    .sudo()
                    .search([("login", "=", qcontext.get("login"))])
                ):
                    qcontext["error"] = _(
                        "Another user is already registered using this email address."
                    )
                else:
                    _logger.error("%s", e)
                    qcontext["error"] = _("Could not create a new account.")

        elif "signup_email" in qcontext:
            user = (
                request.env["res.users"]
                .sudo()
                .search(
                    [
                        ("email", "=", qcontext.get("signup_email")),
                        ("state", "!=", "new"),
                    ],
                    limit=1,
                )
            )
            if user:
                return request.redirect(
                    "/web/login?%s"
                    % url_encode({"login": user.login, "redirect": "/web"})
                )

        response = request.render("auth_signup.signup", qcontext)
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["Content-Security-Policy"] = "frame-ancestors 'self'"
        return response

    def _prepare_signup_values(self, qcontext):
        values = super()._prepare_signup_values(qcontext)
        values["email"] = qcontext.get("email", "")

        return values

    def get_auth_signup_qcontext(self):
        qcontext = super().get_auth_signup_qcontext()
        if login := qcontext.get("login"):
            u = http.request.env["res.users"].sudo().search([("login", "=", login)])
            if u.email:
                qcontext["email"] = u.email

        return qcontext
