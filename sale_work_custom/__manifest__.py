{
    'name': 'Sale Customise',
    'description': 'customise sale order',
    'version': "1.0",
    'author': 'chiku Inc.',
    'company': 'my own Inc.',

    'website': "https://www.github.com//capchi079.com",
    'category': 'Industry',
    'depends': ['base','sale'],
    'data': [
    'security/ir.model.access.csv',
    'security/sale_order_approve_security.xml',
    'views/sale_approve.xml',
    'views/weather.xml',
    'views/deepseek.xml',
    'views/weather_app.xml',
    'views/weather_dashboard_action.xml',
    'views/weather_dashboard_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_work_custom/static/src/js/weather_widget.js',
            'sale_work_custom/static/src/xml/weather_dashboard.xml',
            'sale_work_custom/static/src/video/dash.png',

        ],
    },

    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}