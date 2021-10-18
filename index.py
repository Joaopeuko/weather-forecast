import streamlit as st
from lib.dashboard.utilities import row_creator


import requests
SERVER_URL = 'http://127.0.0.1:5000'

st.set_page_config(layout="wide")

row_title = row_creator(3)
row_title[1].title('Weather Forecast')

row_input = row_creator(3)
city = row_input[1].text_input("Type the City you want to know the weather!")


if len(city) == 0:
    pass

else:
    request_link = f'{SERVER_URL}/weather/{city}'
    row_result = row_creator(3)
    result = requests.get(request_link).json()

    row_result[1].markdown('## {} \n '
                           '### {} \n '
                           '#### {}'.format(result["city"], result["temperature"], result["weather"]))

