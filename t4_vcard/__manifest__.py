# -*- coding: utf-8 -*-
{
    "name": "T4 vCard",
    "summary": """
       Render the data in database to vCard format""",
    "description": """
        This module is used to render the data in database to vcard format
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co/",
    "category": "T4/Vcard",
    "version": "16.0.1.0.0",
    "depends": ["t4", "t4_contact"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/contact_mass_vcard_wizard_view.xml",
        "views/views.xml",
        "views/templates.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
    "application": False,
}
