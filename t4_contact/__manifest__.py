# -*- coding: utf-8 -*-
{
    "name": "T4 Contact",
    "summary": """
        T4 Contact is product of company""",
    "description": """
         T4 Contact is product of company
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
    "license": "LGPL-3",
    "application": True,
}
