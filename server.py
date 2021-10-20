import json
from flask import Flask, request
from lib.openweather import OpenWeather
from flask_caching import Cache

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 5 * 60
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)

cache = Cache(app)

weather = OpenWeather()


@app.route('/weather/<city_name>')
@cache.cached()
def results(city_name):
    result = weather.get_weather_by_city(city_name)
    return result


@app.route('/weather', methods=['GET'])
def max_values():
    if request.args and request.args['max'].isnumeric():
        max_number = int(request.args['max'])
    else:
        max_number = 5

    result = []
    for k in reversed(list(cache.cache._cache.keys())[-max_number:]):
        result.append(cache.get(k))
    return json.dumps(result)


if __name__ == '__main__':
    app.run()
