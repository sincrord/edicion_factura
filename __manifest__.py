# -*- coding: utf-8 -*-

{
    'name': 'Agregar permiso para la Edicion Factura',
    'version': '14.0.1.0',
    'category': 'Accounting',
    'summary': 'Solo permite edición a grupo especial en facturas confirmadas',

    'author': "SINCRO Recursos Digitales",
    'website': "www1.sincro.com.mx",

    'depends': ['account'],
    'data': [
        'views/edicion_factura_group.xml',
        'views/account_move_view.xml'
    ],
    'installable': True,
    'application': False,
}