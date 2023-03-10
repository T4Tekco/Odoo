# -*- coding: utf-8 -*-
{
    "name": "T4 Contact Portal",
    "summary": """Just Portal for external user""",
    "description": """
        Long description of module's purpose
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co/",
    "category": "T4/Contact",
    "version": "16.0.1.0.0",
    "depends": ["t4", "t4_contact", "website_partner"],
    "data": [
        # "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/portal_templates.xml",
        "views/public_templates.xml",
    ],
    "license": "LGPL-3",
    "application": False,
}
