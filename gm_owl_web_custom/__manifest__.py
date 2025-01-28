# -*- encoding: utf-8 -*-
###################################################################
#
#       G. Mostafa
#       Copyright (C) 2024 (https://gmostafa1210.github.io/)
#
###################################################################

{
    'name': 'Basic OWL and Website',
    'version': '18.0.1.0.0',
    'category': 'Website/Website',
    'sequence': -1,
    'summary': 'Basic OWL and Website',
    'description': """
Basic OWL and Website
===========================
Basic OWL and Website for practice in Odoo v18.
    """,
    'author': 'G. Mostafa',
    'website': 'https://gmostafa1210.github.io/',
    'company': 'G. Mostafa',
    'maintainer': 'G. Mostafa',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list_views.xml',
    ],
    # 'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}