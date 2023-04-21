# -*- coding: utf-8 -*-
{
    'name': "OWL TTN",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'tree_view', 'mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/customer_barcode_production.xml',
        'views/owl_templates/owl_customer.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
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
