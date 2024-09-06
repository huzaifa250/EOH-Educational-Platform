# -*- coding: utf-8 -*-
{
    'name': "slide_add",

    'summary': """  It's add Required skills to the contents of course""",

    'description': """
        Cont development for an E-learning App
    """,

    'author': "Huzaifa Elnaeem",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'E-learning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website_slides'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_inherit_slide_form.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}
