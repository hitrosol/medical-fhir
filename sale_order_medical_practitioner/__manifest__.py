{
    'name': 'Sale Order Medical Practitioner',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Add practitioner to sale orders and reports',
    'author': 'PT Solusi Aglis Indonesia',
    'website': 'https:/solusiaglis.co.id',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'medical_administration_practitioner_specialty',
    ],
    'data': [
        'views/sale_order_views.xml',
        'reports/sale_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
