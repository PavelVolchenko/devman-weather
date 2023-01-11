import requests


def weather_forecast():
    cities = ["Лондон", "Череповец", "Москва", "Ростов-на-Дону", "Уфа", "Санкт-Петербург"]
    payload = {
        'm': '',
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
        }

    for city in cities:
        response = requests.get(f'https://wttr.in/{city}', params=payload)
        response.raise_for_status()
        print(response.text)
