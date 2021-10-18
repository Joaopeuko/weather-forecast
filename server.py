from flask import Flask
from lib.openweather import OpenWeather


app = Flask(__name__)
weather = OpenWeather()


@app.route('/weather/<city_name>')
def results(city_name):
    result = weather.get_weather_by_city(city_name)
    return result


if __name__ == '__main__':
    app.run()
