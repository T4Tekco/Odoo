# -*- coding: utf-8 -*-
{
    "name": "T4 Search",
    "summary": """
        Biz  card is product of company, with Biz card you can customize contact card and portfolio website
        """,
    "description": """
        Search User 
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "T4/Search",
    "version": "16.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["t4"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
