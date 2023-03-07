# -*- coding: utf-8 -*-
{
    "name": "bizcard_web",
    "summary": """
        Frontend lam""",
    "description": """
        Ok Luon
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co/",
    "category": "Website/BizCard",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
