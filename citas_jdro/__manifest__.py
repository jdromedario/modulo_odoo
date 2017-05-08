# -*- coding: utf-8 -*-
{
    'name': "citas_jdro - José David Romero SGE4",

    'summary': """
        Citas para tarea SGE 4 """,

    'description': """
        Esta aplicación permite introducir citas de autores
    """,

    'author': "José David Romero",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'test': [],
    'data': ['views/citas_jdro_view.xml',],
    'installable': True,
    'auto_install': False,
}
