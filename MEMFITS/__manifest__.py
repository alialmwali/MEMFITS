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
    'depends': ['contacts', 'project', 'crm'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/customer_catg.xml',
        'views/res_partner.xml',
        'views/leads.xml',
    ],
}
