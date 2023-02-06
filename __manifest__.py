
{
    'name': 'Shrimp Liquidation',
    'version': '1.0',
    'category': 'Sales/Sales',
    'description': "Module for liquidation of shrimp",
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/shrimp_liquidation_views.xml',
        'views/shrimp_menus.xml',
        'views/shrimp_liquidation_config_views.xml',
        'views/inherited_product_template_form_view.xml',
        'views/inherited_purchase_order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
