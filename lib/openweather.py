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
        self.__API_KEY = os.environ.get("API_KEY")

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

    def get_city_temperature(self, city):
        """
        :param city: str
            The city to the desired temperature.
        :return: float
             It returns the Celsius temperature.
        """
        request_link = f'http://api.openweathermap.org/data/2.5/' \
                       f'weather?q={city}&appid={self.__API_KEY}&units=metric'

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
                       f'reverse?lat={geolocation[0]}&lon={geolocation[1]}&limit={limit}&appid={self.__API_KEY}'

        return requests.get(request_link).json()[0]['name']

    def get_weather_by_geolocation(self):
        """
        It uses the function get_city_by_geolocation() to automatically return a dictionary containing city and
        temperature in Celsius
        :return: dict, str: float
            It returns a dictionary containing city and
            temperature in Celsius
        """

        city = self.get_city_by_geolocation()
        city_information = self.get_city_information(city)
        temperature = city_information['main']['temp']
        weather_status = city_information['weather'][0]['main']
        return {'city': city_information['name'], 'weather': weather_status, 'temperature': temperature}

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


if __name__ == '__main__':
    weather = OpenWeather()

    print(weather.get_weather_by_city('flop'))
    # request_link = f'http://api.openweathermap.org/data/2.5/' \
    #                f'weather?q={"sao paulo"}&appid={weather.__API_KEY}&units=metric'

    # print(requests.get(request_link).json())
