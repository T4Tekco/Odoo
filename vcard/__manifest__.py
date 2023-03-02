# -*- coding: utf-8 -*-
{
    'name': "V Card",

    'summary': """
       Render the data in database to vcard format""",

    'description': """
        This module is used to render the data in database to vcard format
    """,

    'author': "T4Tek",
    'website': "https://t4tek.co/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity/Vcard',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['t4contact'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": False,
}
