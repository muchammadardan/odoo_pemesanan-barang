{
    'name': 'Program Skripsi',
    'version': '1.o',
    'summary': 'website_eoq',
    'category': 'Kimia Farma',
    'author': 'Muchammad Ardan',
    'maintainer': 'Muchammad Ardan',
    'website': 'google.com',
    'license': 'Other proprietary',
    'contributors': [
        'Muchammad Ardan',
    ],
    'depends': [
        'web_responsive',
    ],
    # 'external_dependencies': {
    #     'python': [
    #         '',
    #     ],
    # },
    'data': [
        # Security
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',

        # views
        'views/barang.xml',
        'views/barang_masuk_sequence.xml',
        'views/barang_masuk.xml',
        'views/pelanggan.xml',
        'views/nota_sequence.xml',
        'views/transaksi.xml',
        'views/reorder.xml',
        'views/reorder_sequence.xml',
        'views/ramalan.xml',
        'views/ramalan_data.xml',
        'views/laporan.xml',
        'views/pemesanan.xml',
        'views/zmenu.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
