# -*- coding: utf-8 -*-
{
    "name": "Editable Price for Services",
    "version": "17.0.1.0.0",
    "category": "Custom",
    "description": "Es un modulo que le da un comportamiento especial a los productos que son de tipo serivcio.",
    "author": 'Outsource',
    "maintainer": "",
    'depends': ['sale', 'purchase', 'account'],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_line_views.xml",
        "views/purchase_order_line_views.xml",
        "views/sale_order_line_views.xml",
    ],
    "assets": {},
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True
}