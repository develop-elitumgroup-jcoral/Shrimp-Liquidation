{
    'name': 'Shrimp Liquidation',
    'version': '1.0',
    'category': 'Shrimp/Liquidation',
    'description': "Module for liquidation of shrimp",
    'depends': ['base', 'product', 'stock', 'stock_landed_costs', 'web_domain_field'],
    'data': [
        'security/shrimp_liquidation_security.xml',
        'security/ir.model.access.csv',
        'views/stock_move_views.xml',
        'views/shrimp_liquidation_views.xml',
        'views/shrimp_liquidation_config_views.xml',
        'views/inherited_product_template_form_view.xml',
        'views/inherited_purchase_order_view.xml',
        'views/res_config_settings_views.xml',
        'views/stock_landed_cost_views.xml',
        'views/shrimp_menus.xml',

    ],
    'qweb': [
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
