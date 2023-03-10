# -*- coding: utf-8 -*-
{
    "name": "T4 Suneditor WYSIWYG",
    "summary": """
        Add Suneditor WYSIWYG""",
    "description": """Hello World""",
    "author": "T4Tek Team",
    "website": "https://t4tek.co/",
    "category": "T4/HTMLEditor",
    "version": "16.0.1.0.0",
    "depends": ["t4", "web"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "t4_suneditor_wysiwyg/static/src/suneditor/**/*",
            "t4_suneditor_wysiwyg/static/src/js/**/*",
        ],
        "web.assets_frontend": [
            "t4_suneditor_wysiwyg/static/src/suneditor/**/*",
            "t4_suneditor_wysiwyg/static/src/js/**/*",
        ],
    },
    "license": "LGPL-3",
    "application": False,
}
