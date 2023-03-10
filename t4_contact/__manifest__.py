# -*- coding: utf-8 -*-
{
    "name": "T4 Contact",
    "summary": """
        Biz  card is product of company, with Biz card you can customize contact card and portfolio website""",
    "description": """
         Biz  card is product of company, with Biz card you can customize contact card and portfolio website
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co",
    "category": "T4/Contact",
    "version": "16.0.1.0.0",
    "depends": ["t4"],
    "data": [
        "security/t4_contact_security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/contact_view.xml",
        "views/industry_view.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
    "application": True,
}
