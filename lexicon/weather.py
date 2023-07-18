# Возвращает шаблон заполнения погоды
def get_weather_text(dct: dict):
    if dct['cod'] == 200:
        return f'Погода в городе {dct["city"]}.\n\n' \
               f'За окном {dct["description"]}.\n' \
               f'На улице: {dct["temp"]}C°.\n' \
               f'По ощущениям: {dct["temp_feels_like"]}C°.\n' \
               f'Скорость ветра: {dct["wind_speed"]}м/с.\n' \
               f'Влажность воздуха составляет: {dct["humidity"]}%.\n'
    else:
        return 'Похоже в моей базе нет такого города'