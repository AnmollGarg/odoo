{
    'name': 'Free Shipping Product Fix for Loyalty',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Prevents duplicating the Free Shipping product for loyalty rewards',
    'description': """
        This module overrides the standard behavior of the Odoo Loyalty module for free shipping rewards.
        By default, Odoo creates a new 'Free Shipping' product for every single free shipping loyalty reward you create, cluttering your catalog. 
        This module fixes this issue by reusing an existing product with the exact same name for all matching free shipping rewards.
    """,
    'author': 'Anmol Garg',
    'depends': ['sale_loyalty_delivery', 'loyalty'],
    'data': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'price': 1.0,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
}
