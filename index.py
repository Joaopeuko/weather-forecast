import streamlit as st
import requests


def row_creator(columns_numbers):
    """
    columns_numbers is the amount of columns that you want to have in a row.

    :param columns_numbers:
    :return row:
    """
    row = st.columns(columns_numbers)
    for _ in range(len(row)):
        row[_] = row[_].empty()

    return row


def get_cached(SERVER_URL, max_number=5):
    return requests.get(f'{SERVER_URL}/weather?max={max_number}').json()


def single_display(result, row_result):
    row_result.metric(str(result["city"]), str(result["temperature"]) + " C°", result["weather"], delta_color='off')


def cached_display(cached_list, row_result):
    for index, reversed_index in enumerate(reversed(range(len(cached_list)))):
        single_display(cached_list[reversed_index], row_result[index])


SERVER_URL = 'http://127.0.0.1:5000'

# Page layout configuration
st.set_page_config(layout="centered")

# It creates the first row to hold the title
row_title = row_creator(1)
row_title[0].title('Weather Forecast')

# It creates the second row to hold the city input
row_input = row_creator(1)
city = row_input[0].text_input("Type the City you want to know the weather!")  # The city variable holds the input value

weather_cached = get_cached(SERVER_URL, 5)

# It creates the row that will display single results, the error message if
# the city do not exist or the weather forecast
single_result = row_creator(1)  # The number of columns 7 is for style porpoise

# It creates the row that will display all the results with max number set by user,
# # max default is 5.
st.write("<br>", unsafe_allow_html=True)
row_result = row_creator(len(weather_cached) + 1)

if len(city) == 0:
    pass

else:
    result = requests.get(f'{SERVER_URL}/weather/{city.lower()}')

    if result.status_code == 404:
        single_result[0].write("<font color='red'> Sorry. We couldn't find specified city. </font >",
                               unsafe_allow_html=True)

    else:
        single_display(result.json(), single_result[0])  # It returns the last searched information

cached_display(weather_cached, row_result=row_result)
