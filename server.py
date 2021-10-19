from flask import Flask, request
from lib.openweather import OpenWeather

app = Flask(__name__)
weather = OpenWeather()


@app.route('/weather/<city_name>')
def results(city_name):
    result = weather.get_weather_by_city(city_name)
    return result


@app.route('/weather', methods=['GET'])
def max_values():
    default = 5
    print(len(request.args))
    if not request.args or not request.args['max'].isnumeric():
        return str(default)
    else:
        return request.args['max']


if __name__ == '__main__':
    app.run()
