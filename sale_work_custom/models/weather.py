
from odoo import fields,models,api
import requests

class WeatherApp(models.Model):

    _name='weather.app'
    _rec_name = 'city'
    user = fields.Many2one('res.partner', string='User')
    city = fields.Char(string='City')
    zip_pin=fields.Integer(string='PinCode')
    weather=fields.Char(string='weather')




    def get_weather(self):
        api_key='f76ec463513c7b3cbdd2357f584d073f'
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        for rec in self:
            # if not rec.city:
            #     continue
            if rec.city:
                 argu={
                'q': rec.city,
                'appid': api_key,
                'units': 'metric'
            }
            else:
                argu = {
                    'q': rec.zip_pin,
                    'appid': api_key,
                    'units': 'metric'
                }
            try:
                response = requests.get(base_url, params=argu, timeout=10)
                data = response.json()
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                rec.weather = f"{temp}°C, {description}"
            except requests.exceptions.RequestException as e:
                print(e)

