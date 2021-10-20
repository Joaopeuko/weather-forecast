import os
import requests
from dotenv import load_dotenv


class OpenWeather:
    """
    A class is used to handle all the functions needed from the Open Weather API.
    """

    def __init__(self):
        load_dotenv()
        self.__API_KEY = os.environ.get("API_KEY")

    def get_weather_by_city(self, city):
        """
        :param city: str
            It uses the city to return the weather of desired location.
        :return: float
             It returns the weather, like if is sunny or raining.
        """
        city_information = self.get_city_information(city)
        if city_information['cod'] == '404':
            return {'city': 'city_name_invalid', 'weather': 'single_result', 'temperature': 'single_result'}
        else:
            temperature = city_information['main']['temp']
            weather_status = city_information['weather'][0]['main']
            return {'city': city_information['name'], 'weather': weather_status, 'temperature': temperature}

    def get_city_information(self, city):
        """
        :param city: str
            The city to the desired temperature.
        :return: float
             It returns the Celsius temperature.
        """
        request_link = f'http://api.openweathermap.org/data/2.5/' \
                       f'weather?q={city}&appid={self.__API_KEY}&units=metric'

        return requests.get(request_link).json()
