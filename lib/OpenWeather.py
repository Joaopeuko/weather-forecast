from dotenv import load_dotenv
import os

import geocoder

import requests


class OpenWeather:
    """
    A class is used to handle all the functions needed from the Open Weather API.
    """

    def __init__(self):
        load_dotenv()
        self.API_KEY = os.environ.get("API_KEY")

    def get_city_temperature(self, city):
        """
        :param city: str
            The city to the desired temperature.
        :return: float
             It returns the Celsius temperature.
        """
        request_link = f'http://api.openweathermap.org/data/2.5/' \
                       f'weather?q={city}&appid={self.API_KEY}&units=metric'

        return requests.get(request_link).json()['main']['temp']

    def get_city_by_geolocation(self):
        """
        It uses the IP address to return the geolocation and return the City.
        :return: str
            It returns the City name by determining geolocation.
        """
        limit = 1
        geolocation = geocoder.ip('me').latlng  # return a list containing latitude and longitude
        request_link = f'http://api.openweathermap.org/geo/1.0/' \
                       f'reverse?lat={geolocation[0]}&lon={geolocation[1]}&limit={limit}&appid={self.API_KEY}'

        return requests.get(request_link).json()[0]['name']

    def get_temperature_by_geolocation(self):
        """
        It uses the function get_city_by_geolocation() to automatically return a dictionary containing city and
        temperature in Celsius
        :return: dict, str: float
            It returns a dictionary containing city and
            temperature in Celsius
        """
        city = self.get_city_by_geolocation()
        return {city: self.get_city_temperature(city)}
