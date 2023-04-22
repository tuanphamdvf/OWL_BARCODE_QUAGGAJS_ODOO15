# -*- coding: utf-8 -*-
{
    'name': "Barcode mrp production",
    "version": "15",
    "summary": "Ứng dụng quét mã đơn sản xuất, chuyển hướng đến đơn sản xuất đó",
    'description': """
      Ứng dụng quét mã vạch của đơn sản xuất, và chuyển hướng đến đơn sản xuất đó, giúp hỗ trợ cho việc chuyển ca, nhân viên có thể quét mã và sẽ biết trạng thái của các lệnh sản xuất đang được thực hiện dở dang !!
    """,
    "price": "1000000",
    "currency": "VND",

    'author': "tuanphamdvf",
    'website': "TTNSOFTWARE.STORE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.2.1',

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
