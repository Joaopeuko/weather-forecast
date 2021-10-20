import streamlit as st
import requests


def row_creator(columns_numbers):
    """
    It creates the X amount of columns that one wants to have in a row.

    :param columns_numbers: int
        It contains the number of columns a row will have.
    :return row: streamlit.columns
        row with X number of columns:
    """
    row = st.columns(columns_numbers)
    for _ in range(len(row)):
        row[_] = row[_].empty()

    return row


def get_cached(SERVER_URL, max_number=5):
    """
        It asks for the server for X amount of data cached on the server.
    :param SERVER_URL: string
        A string that contains the server address.
    :param max_number: int
        The amount of information the user desire from cached data.
    :return: json
        It returns a JSON containing the last X amount of data.
    """
    return requests.get(f'{SERVER_URL}/weather?max={max_number}').json()


def single_display(result, row_result):
    """
    This function receives the information returned from the server to display it only one time.
    :param result: dict
        A dictionary containing information about the weather in a determined city.
    :param row_result: streamlit column
        It receives the column slot to be filled with the information.
    :return:
    """
    row_result.metric(str(result["city"]), str(result["temperature"]) + " C°", result["weather"], delta_color='off')


def cached_display(cached_list, row_result):
    """
    This function receives the information cached returned from the server to display.
    :param cached_list: list
        A list containing many dictionaries of the last searches.
    :param row_result: list of streamlit columns
        A list of streamlit columns to fill with information.
    :return:
    """
    for index, reversed_index in enumerate(reversed(range(len(cached_list)))):
        single_display(cached_list[reversed_index], row_result[index])


SERVER_URL = 'http://127.0.0.1:5000'  # The server address in localhost.

# Page layout configuration.
st.set_page_config(layout="centered")

# It creates the first row to hold the title.
row_title = row_creator(1)
row_title[0].title('Weather Forecast')

# It creates the second row to hold the city input.
row_input = row_creator(1)
# The city variable holds the input value.
city = row_input[0].text_input("Type the City you want to know the weather!")

# It gets all the information cached.
weather_cached = get_cached(SERVER_URL, 5)

# It creates the row that will display single results and the error message if
# the city does not exist in the weather forecast or some information was wrongly provided.
single_result = row_creator(1)  # The number of columns 7 is for style reasons

# It inserts a blank space between a single result and the row with many results.
# It is for style reasons
st.write("<br>", unsafe_allow_html=True)

# It creates the row that will display all the results with max_number set by the user,
# # max default is 5.
row_result = row_creator(len(weather_cached) + 1)

# If no information is passed through the input nothing happens.
if len(city) == 0:
    pass

else:
    # It requests the weather information for a determined city.
    result = requests.get(f'{SERVER_URL}/weather/{city.lower()}')

    # If the result is not a city it displays an error message.
    if result.status_code == 404:
        single_result[0].write("<font color='red'> Sorry. We couldn't find the specified city. </font >",
                               unsafe_allow_html=True)

    else:
        # If the result is what is expected it displays the city weather.
        single_display(result.json(), single_result[0])  # It returns the last searched information

# It displays all the last X number of cached information.
cached_display(weather_cached, row_result=row_result)
