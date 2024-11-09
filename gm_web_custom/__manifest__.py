# -*- encoding: utf-8 -*-
###################################################################
#
#       G. Mostafa
#       Copyright (C) 2024 (https://gmostafa1210.github.io/)
#
###################################################################

{
    'name': 'Web Customization',
    'version': '18.0.1.0.0',
    'category': 'Website/Website',
    'sequence': 1,
    'summary': 'Web Customization',
    'description': """
Web Customization
===========================
Web customization for practice in Odoo v18.
    """,
    'author': 'G. Mostafa',
    'website': 'https://gmostafa1210.github.io/',
    'company': 'G. Mostafa',
    'maintainer': 'G. Mostafa',
    'depends': ['base', 'contacts', 'website', 'portal'],
    'data': [
        'views/res_partner_website_views.xml',
    ],
    # 'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}