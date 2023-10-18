import requests
import argparse


def get_weather(city):
    payload = {
        'm': '',
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru',
    }
    response = requests.get(f'https://wttr.in/{city}', params=payload)
    response.raise_for_status()
    weather_forecast = response.text
    return weather_forecast


if __name__ == '__main__':
    cities = ['Лондон', 'Череповец', 'Шереметьево']
    [print(get_weather(city)) for city in cities]
