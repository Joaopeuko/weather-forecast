import streamlit as st
import extra_streamlit_components as stx

from lib.dashboard.utilities import row_creator
import datetime

from collections import deque

import requests
import pandas as pd

from lib.dashboard.utilities import last_search_display, set_cookie, single_display

SERVER_URL = 'http://127.0.0.1:5000'
COOKIE_EXPIRATION_TIME = 5  # minutes

# Page layout configuration
st.set_page_config(layout="wide")

# It creates the first row to hold the title
row_title = row_creator(3)
row_title[1].title('Weather Forecast')

# It creates the second row to hold the city input
row_input = row_creator(3)
city = row_input[1].text_input("Type the City you want to know the weather!")  # The city variable holds the input value

row_buttons = row_creator(3)
last_button = row_creator(24)
button_position = 11  # For style porpoise
last_button[button_position + 1].write('Display: ')
button_3 = last_button[button_position + 2].button('3')
button_5 = last_button[button_position + 3].button('5')
button_7 = last_button[button_position + 4].button('7')

max_number_request_link = f'{SERVER_URL}/weather'
max_number = requests.get(max_number_request_link).json()

print(max_number)

cookie_manager = stx.CookieManager()


def set_max_number(number):
    cookie_manager.set('max_number', number,
                       expires_at=(datetime.datetime.now() + datetime.timedelta(
                           minutes=COOKIE_EXPIRATION_TIME)))


def get_max_number():
    max_number_request = f'{SERVER_URL}/weather'
    number_result = requests.get(max_number_request).json()
    return number_result


if button_3:
    max_number = 3

elif button_5:
    max_number = 5

elif button_7:
    max_number = 7

set_max_number(max_number)
MAX_NUMBER_COOKIE = cookie_manager.get('max_number')
if MAX_NUMBER_COOKIE is None:
    max_number_request_link = f'{SERVER_URL}/weather'
    max_number = requests.get(max_number_request_link).json()
else:
    max_number = MAX_NUMBER_COOKIE

single_result = row_creator(7)
row_result = row_creator(max_number)

last_search_display(max_number, row_result)  # It returns all the information with max set by user,
# max default is 5.

if len(city) == 0:
    pass

else:
    request_link = f'{SERVER_URL}/weather/{city.lower()}'
    result = requests.get(request_link).json()

    if result is not None:
        if result['city'] == 'city_name_invalid':

            single_result[3].write("Sorry. We couldn't find specified city.")
            last_search_display(max_number, row_result)  # It returns all the information with max set by user,
            # max default is 5.

        else:
            set_cookie(result, max_number)  # It saves the new valid information
            single_display(result, single_result)  # It returns the last searched information
            last_search_display(max_number, row_result)  # It returns all the information with max set by user,
            # max default is 5.
