# -*- coding: utf-8 -*-
{
    'name': "Medical Appointment Invoices",

    'summary': """
        Generate invoices from medical appointments when there are "done".
        """,

    'description': """
        This module generate automatic invoice for patient when an appointment is done.
    """,

    'author': "Business Agile",
    'website': "http://businessagile.eu/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'medical'],
    
    # "update_xml": [
    #     "views/medical_invoice_view.xml",
        # "views/appointment_invoice.xml",
    # ],
}