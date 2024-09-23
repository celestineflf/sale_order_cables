# -*- coding: utf-8 -*-
{
    'name' : 'Sale Order Cables',
    'version' : '1.0',
    'summary': 'Cable making',
    'sequence': -100,
    'description': """
Cable making module for Sales order
    """,
    'author': 'Celestine Dabrowski',
    'category': 'Productivity',
    'images' : [],
    'depends' : ['sale', 'mrp', 'product', 'stock'],
    'data': [
        'views/product_extend.xml',
        'views/sale_extend.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'OPL-1',
}
