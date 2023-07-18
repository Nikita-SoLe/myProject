import requests
import pprint

_params = {
    'units': 'metric',
    'lang': 'ru'
}


# Возвращает словарь погоды
def _get_weather(data: dict):

    dct = {}

    if int(data['cod']) == 200:
        dct['cod'] = data['cod']
        dct['city'] = data['name']
        dct['temp'] = int(data['main']['temp'])
        dct['temp_feels_like'] = int(data['main']['feels_like'])
        dct['humidity'] = data['main']['humidity']
        dct['wind_speed'] = round(data['wind']['speed'], 1)
        dct['description'] = str(data['weather'][0]['description'])

        return dct
    return data


# Возвращает словарь с погодой по названию города
def weather_get_city(city, open_weather_token) -> dict | str:

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}',
                                params=_params)

    data = response.json()

    pprint.pprint(data)

    return _get_weather(data)


# Возвращает словарь с погодой по геоданным
def location_weather(lat, lon, open_weather_token):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}',
        params=_params
    )

    data = response.json()

    return _get_weather(data)
