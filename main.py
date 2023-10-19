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
    return response.text


if __name__ == '__main__':
    cities = ['Лондон', 'Череповец', 'Шереметьево']
    for city in cities:
        print(get_weather(city))
