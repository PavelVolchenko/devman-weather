import requests
import argparse


def get_weather(city):
    payload = {
        'm': '',
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }
    response = requests.get(f'https://wttr.in/{city}', params=payload)
    response.raise_for_status()
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скрипт получения прогноза погоды. ")
    parser.add_argument('city', help='Название города (латиница/кириллица)')
    args = parser.parse_args()
    weather = get_weather(city=args.city)
    print(weather.text)
