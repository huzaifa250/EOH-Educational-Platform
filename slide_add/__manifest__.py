# -*- coding: utf-8 -*-
{
    'name': "slide_add",

    'summary': """extended E-learning app""",

    'description': """
        add new features to an E-learning app :
        - edit course contents by adding required skills for specifc course
        - ensure required skills are met
        - enable extrnal users to access courses from website and add specific course as well 
    """,

    'author': "Huzaifa Elnaeem",
    'website': "huz.dark1@gmail.com",

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
        'views/courses_controller_temp.xml',
        'views/new_coures_conteroller.xml',
        # 'views/custom_config_setting.xml',

    ],
    'images': ['static/description/learning_6555186.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}
