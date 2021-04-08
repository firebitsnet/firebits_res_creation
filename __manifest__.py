{
    'name': 'FireBits Resources Creation',
    'version': '13.0.0.1',
    'summary': 'Limit creation access for partners and products to specific users',
    # 'description': '''
    # ''',
    'category': 'Resources',
    'author': 'FireBits',
    'sequence':-52,
    'website': 'https://firebits.net',
    # 'license': '',
    'depends': [
        'base',
        'product'
    ],
    'data': [
        'security/groups.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}