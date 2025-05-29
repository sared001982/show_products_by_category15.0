# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'SHOW PRODUCTS GROUPED BY CATEGORY ON SALE ORDER REPORT ',
"author": "REDOUANE SAKTY",
    "version": "15.0.1.0",
    'category': 'SALE',
    'sequence': 1,
    'summary': 'THIS MODULE ALLOWS YOU TO SHOW YOUR SALE ORDER LINES GROUPED BY PRODUCT CATEGORY. AND SHOW ON THE HEAD OF EACH CATEGORY ARTICLES? THE CATEGORY  ',
    'website': 'sared001@gmail.com',
    'depends': ['base', 'sale'],
    'data': [
        'report/report_purchaseorder.xml',
    ],
    "license": "OPL-1",
    "currency":"EUR",
    "price": 9.99,
    "installable" : True,
    "auto_install" : False,
    "application" : True,
    "demo": [],
    "test": [],
    "images": [
        "static/src/img/icon.png",
        "static/description/icon.png",
    ],
    "assets": {
    },

}
