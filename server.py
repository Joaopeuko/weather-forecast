import json
from flask_caching import Cache
from flask import Flask, request, abort
from lib.openweather import OpenWeather

config = {
    "DEBUG": True,  # Some Flask-specific configurations..
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configuration.
    "CACHE_DEFAULT_TIMEOUT": 5 * 60  # Time, 60 seconds time 5.
}
app = Flask(__name__)  # It creates the Flask App


# Tell Flask to use the above-defined config
app.config.from_mapping(config)

cache = Cache(app)  # It handles the cache for the server-side.

weather = OpenWeather()  # It creates the class to handle Open Weather.


@app.route('/weather/<city_name>')
@cache.cached()
def results(city_name):
    """
    The function receives a string containing a city name and returns the weather information.
    Also, it caches the information.
    :param city_name: str
        It receives a request from the front end containing a city name.
    :return: dict
        returns a dictionary containing information about the weather of a determined city.

    """
    result = weather.get_weather_by_city(city_name)

    if result['city'] == 'city_name_invalid' or str(city_name).isnumeric():
        abort(404)  # In case the city name is invalid it returns an error 404.

    return result


@app.route('/weather', methods=['GET'])
def max_values():
    """
    These functions handle the max amount of information needed to be returned to the user from the cached information.
    If the amount of information
    :return: json
        It returns a JSON that contains a dictionary about the last results.
    """

    if 'max' in list(request.args.keys()) and request.args['max'].isnumeric():
        max_number = int(request.args['max'])  # It returns the new amount of information the users requested.
    else:
        max_number = 5  # The default amount of data returned.

    result = []
    # It retrieves the newest amount of data requested.
    for key in reversed(list(cache.cache._cache.keys())[-max_number:]):
        result.append(cache.get(key))
    return json.dumps(result)


if __name__ == '__main__':
    app.run()  # It runs the server.
