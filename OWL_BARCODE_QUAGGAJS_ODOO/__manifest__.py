# -*- coding: utf-8 -*-
{
    'name': "Barcode production",
    "summary": "Barcode scanner production",
    'description': """The barcode scanning application of the production order can redirect to that production order, supporting the shift change process. Employees can scan the code and know the status of the unfinished production orders!!
    """,
    "price": "19",
    "currency": "EUR",

    'author': "TTN SOFTWARE",
    'website': "TTNSOFTWARE.STORE",
    'category': 'App',
    'version': '15.1.1',
    'depends': ['base', 'mrp'],

    'data': [
        'security/ir.model.access.csv',
        'report/customer_barcode_production.xml',
        'views/owl_templates/owl_customer.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'OWL_BARCODE_QUAGGAJS_ODOO/static/src/xml/*',
        ],
        'web.assets_backend': [
            'OWL_BARCODE_QUAGGAJS_ODOO/static/src/components/**/*',
            'OWL_BARCODE_QUAGGAJS_ODOO/static/src/scss/**/*',
            'OWL_BARCODE_QUAGGAJS_ODOO/static/lib/*',
            'OWL_BARCODE_QUAGGAJS_ODOO/static/src/js/**/*',
            'OWL_BARCODE_QUAGGAJS_ODOO/static/src/js/*',
        ],

    }
}
