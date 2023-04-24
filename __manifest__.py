# -*- coding: utf-8 -*-
{
    'name': "Barcode mrp production",
    "summary": "Ứng dụng quét mã đơn sản xuất",
    'description': """
      Ứng dụng quét mã vạch của đơn sản xuất, và chuyển hướng đến đơn sản xuất đó, giúp hỗ trợ cho việc chuyển ca, nhân viên có thể quét mã và sẽ biết trạng thái của các lệnh sản xuất đang được thực hiện dở dang !!
    """,
    "price": "0",
    "currency": "VND",

    'author': "tuanphamdvf",
    'website': "TTNSOFTWARE.STORE",
    'license': 'LGPLv3',
    'category': 'Uncategorized',
    'version': '1.2.1',
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
