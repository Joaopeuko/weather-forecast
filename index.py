import streamlit as st
import extra_streamlit_components as stx

from lib.dashboard.utilities import row_creator
import datetime

from collections import deque

import requests
import pandas as pd

SERVER_URL = 'http://127.0.0.1:5000'

st.set_page_config(layout="wide")

row_title = row_creator(3)
row_title[1].title('Weather Forecast')

row_input = row_creator(3)
city = row_input[1].text_input("Type the City you want to know the weather!")

cookie_manager = stx.CookieManager()
cookie_list = deque(maxlen=5)
if len(city) == 0:
    pass

else:
    request_link = f'{SERVER_URL}/weather/{city.lower()}'
    row_result = row_creator(3)
    result = requests.get(request_link).json()

    if result is not None:
        cookie_manager_list = cookie_manager.get('WeatherCookie')
        if cookie_manager_list is not None:
            for cookie in cookie_manager_list:
                cookie_list.append(cookie)

            print(result['city'], pd.DataFrame(cookie_manager_list)['city'].values)
            if result['city'] not in pd.DataFrame(cookie_manager_list)['city'].values:
                cookie_list.append(result)
        else:
            cookie_list.append(result)

        cookie_manager.set('WeatherCookie', list(cookie_list),
                           expires_at=datetime.datetime(year=datetime.datetime.now().year,
                                                        month=datetime.datetime.now().month,
                                                        day=datetime.datetime.now().day,
                                                        minute=datetime.datetime.now().minute + 5))

        for last_weather in reversed(range(len(cookie_list))):
            st.markdown('## {} \n '
                        '### {} C° \n '
                        '#### {}'.format(str(cookie_list[last_weather]["city"]).title(),
                                         cookie_list[last_weather]["temperature"],
                                         cookie_list[last_weather]["weather"]))
