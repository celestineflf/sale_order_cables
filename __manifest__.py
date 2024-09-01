# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Cables',
    'version': '15.0',
    'category': 'Warehouse',
    'summary': 'Custom Cables',

    'depends': ['sale_management', 'sale_stock','web_enterprise', 'lightspeed_connector_cr', 'sale_order', 'product_product', 'mrp_production'],

    'data': [
        'views/product.xml',
        'views/stock_location_route.xml',
        'views/sale.xml',
        'views/stock_picking_type.xml',
        'views/tax_view.xml',
        'views/stock_picking.xml',
        'views/partner_view.xml',
    ],

    'assets': {
        'web.assets_backend': [
            '/sale_extended/static/src/css/backend.scss',
        ],
        'web._assets_secondary_variables': [
            '/sale_extended/static/src/css/secondary_variables.scss',
        ],
    },

    'author': 'TeqStars',
    'website': 'https://teqstars.com',
    'support': 'support@teqstars.com',
    'maintainer': 'TeqStars',

    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}

