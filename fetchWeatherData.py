from requests import *
from weather import *

__API = 'a6c974d0246a07438eecd704b695d6061'


def get_weather(city):
    query = 'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API}'
    query = query.format(city=city, API=__API)
    result = get(query)
    weater_obj = Weather('ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR')
    if result.status_code == 200:
        result = result.json()
        name = result['name']
        temperature = result['main']['temp']
        pressure = result['main']['pressure']
        humidity = result['main']['humidity']
        wind_speed = result['wind']['speed']
        country = result['sys']['country']
        weather = result['weather'][0]['description']
        weather_obj = Weather(name, weather, temperature, pressure, humidity, country, wind_speed)
        return weather_obj
    else:
        return weater_obj
