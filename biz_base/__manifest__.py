# -*- coding: utf-8 -*-
{
    "name": "Biz Card",
    "summary": """
        Biz  card is product of company, with Biz card you can customize contact card and portfolio website""",
    "description": """
         Biz  card is product of company, with Biz card you can customize contact card and portfolio website
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co",
    "category": "Productivity/BizCard",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/biz_security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/industry_view.xml"
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
}
