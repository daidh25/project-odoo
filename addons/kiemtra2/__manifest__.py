# -*- coding: utf-8 -*-
{
    'name': "kiemtra2",

    'summary': """
        Thực hành lập trình Odoo""",

    'description': """
        Học lập trình Odoo - Hệ quản trị doanh nghiệp điện từ ERP
    """,

    'author': "Đinh Huy Đại",
    'website': "https://www.google.com.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hệ thống thông tin',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/phong_views.xml',
        'views/nhanvien_views.xml',
        'views/menu_action_views.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/nhanvien_demo.xml',
        'demo/phong_demo.xml',
    ],
}
