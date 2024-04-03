# -*- coding: utf-8 -*-
{
    'name': "Technical Order Application",
    'version': '1.0',
    'description': 'Technical Order Module',
    'author': "Ahmed Abd Elnasser",
    'license': 'LGPL-3',
    'category': 'Sales',
    'sequence': 1 ,
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/security.xml',
        'data/technical_order_sequence.xml',
        'view/partner_views.xml',
        'view/technical_order_views.xml',
        'view/report_technical_order.xml',
    ],

    'auto_install': False,
    'application': True,

}