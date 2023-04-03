# -*- coding: utf-8 -*-
{
    "name": "T4 Statistic",
    "summary": """
        Contact Statistic""",
    "description": """
        Trời tối.
    """,
    "author": "T4Tek Team",
    "website": "https://github.com/T4Tekco/Odoo",
    "category": "T4/Statistic",
    "version": "16.0.1.0.0",
    "depends": ["t4", "t4_contact"],
    "data": [
        "data/track_type.xml",
        "security/t4_track_security.xml",
        "security/ir.model.access.csv",
        "views/statistic_view.xml",
        "views/statistic_menu.xml",
        "views/snippets/snippets.xml",
        "views/snippets/dynamic_snippet_statistic_keyword.xml",
        "views/snippets/dynamic_snippet_statistic_industry.xml",
        "views/snippets/dynamic_snippet_statistic_mainpage.xml",
        "views/snippets/dynamic_snippet_statistic_contact.xml",
    ],
}
