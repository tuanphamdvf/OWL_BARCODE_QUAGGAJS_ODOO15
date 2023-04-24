# -*- coding: utf-8 -*-
{
    'name': "Barcode production",
    "summary": "Barcode scanner production",
    'description': """The barcode scanning application of the production order can redirect to that production order, supporting the shift change process. Employees can scan the code and know the status of the unfinished production orders!!
    """,
    "price": "19",
    "currency": "EUR",

    'author': "tuanphamdvf",
    'website': "TTNSOFTWARE.STORE",
    'license': 'LGPLv3',
    'category': 'App',
    'version': '15.1.1',
    'demo_video_url': "https://www.youtube.com/watch?v=cHSC64DiXoo",
    'depends': ['base', 'tree_view', 'mrp'],

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
            'OWL/static/src/xml/*',
        ],
        'web.assets_backend': [
            'OWL/static/src/components/**/*',
            'OWL/static/src/scss/**/*',
            'OWL/static/lib/*',
            'OWL/static/src/js/**/*',
            'OWL/static/src/js/*',
        ],

    }
}
