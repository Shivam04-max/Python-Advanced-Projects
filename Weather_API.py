import json
import requests
from typing import Final
from model import Weather, dt

API_KEY: Final[str] = 'fb1a6b9affccabb4bb7589c392e2d29f'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city_name: str, mock: bool = False) -> dict:
    if mock:
        print('Using mock data...')
        with open('dummy_data.json') as file:
            return json.load(file)
        
    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request =requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()
    return data

def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')
    
    if not days:
        raise Exception(f'Problem with json: {weather}')
    
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)
    return list_of_weather