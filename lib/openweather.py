import os
import requests
from dotenv import load_dotenv


class OpenWeather:
    """
    Open Weather class is used to handle all the functions needed for the Open Weather API.
    """

    def __init__(self):
        load_dotenv()
        self.__API_KEY = os.environ.get("API_KEY")  # It retrieve my public key located in a .env file for security.

    def get_weather_by_city(self, city):
        """
        :param city: str
            Receives a string that contains the city name to require information.
        :return: dict
             It returns a dictionary containing the city name, the weather, and the temperature in Celsius.
        """

        # It used the function get_city_information to call the Open Weather API
        city_information = self.get_city_information(city)

        if city_information['cod'] == '404':  # It checks if the information returned is valid or not.
            return {'city': 'city_name_invalid', 'weather': 'single_result', 'temperature': 'single_result'}
        else:

            # It retrieves the temperature from returned Open Weather
            temperature = city_information['main']['temp']
            # It retrieves the weather from returned Open Weather
            weather_status = city_information['weather'][0]['main']

            return {'city': city_information['name'], 'weather': weather_status, 'temperature': temperature}

    def get_city_information(self, city):
        """
        :param city: str
            Receives a string that contains the city name to require information.
        :return: dict
             It returns a dictionary containing all the information returned from the Open Weather API
        """
        request_link = f'http://api.openweathermap.org/data/2.5/' \
                       f'weather?q={city}&appid={self.__API_KEY}&units=metric'

        return requests.get(request_link).json()
