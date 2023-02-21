# -*- coding: utf-8 -*-
{
    'name': "MEMFITS",

    'summary': """Custem MEMF""",

    'description': """
       
    """,

    'version': '16.0.0.1',
    'author': '',
    'company': "freelancer",
    'website': '',
    'license': 'LGPL-3',
    #'category': ['HR','Accounting','POS','Health','Report','Stock','Project','Web','Manufacturing','Other',],
    'category': '',
    # any module necessary for this one to work correctly
    'depends': ['contacts', 'project', 'crm', 'sale', 'repair', 'hr_expense', 'purchase', 'delivery'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/customer_catg.xml',
        'views/res_partner.xml',
        'views/leads.xml',
        'views/purchase.xml',
        'views/sale_order.xml',
        'reports/layouts.xml',
        'reports/invoice_report.xml',
        'reports/quotation_sale.xml',
        'reports/stock_delivery.xml',
    ],
}
