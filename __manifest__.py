# -*- coding: utf-8 -*-
{
    'name': "Logros odoo",

    'summary': """
        Pequeña aplicacion que implementa logros en odoo""",

    'description': """
        
    """,

    'author': "A19GabrielBI",
    'website': "https://github.com/A19GabrielBI/logros_odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/logros.xml',
        'views/historial.xml',
        'views/employee.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
