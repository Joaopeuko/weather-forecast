import datetime
import pandas as pd
import streamlit as st
from collections import deque
import extra_streamlit_components as stx


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


def last_search_display(max_display, row_result):
    cookie_manager = stx.CookieManager()

    cookie_list = deque(maxlen=max_display)

    cookie_manager_list = cookie_manager.get('WeatherCookie')
    if cookie_manager_list is not None:
        for cookie in cookie_manager_list:
            cookie_list.append(cookie)

    for index, reversed_index in enumerate(reversed(range(len(cookie_list)))):
        row_result[index].markdown('## {} \n '
                                   '### {} C° \n '
                                   '#### {}'.format(str(cookie_list[reversed_index]["city"]).title(),
                                                    cookie_list[reversed_index]["temperature"],
                                                    cookie_list[reversed_index]["weather"]))


def single_display(result, row_result):
    row_result[3].markdown('## {} \n '
                           '### {} C° \n '
                           '#### {}'.format(str(result["city"]).title(),
                                            result["temperature"],
                                            result["weather"]))


def cookie_len():
    cookie_manager = stx.CookieManager()
    return len(cookie_manager.get('WeatherCookie'))


def set_cookie(result,
               max_number,
               cookie_expiration_time=5):  # In minutes

    cookie_manager = stx.CookieManager()
    cookie_list = deque(maxlen=max_number)

    cookie_manager_list = cookie_manager.get('WeatherCookie')
    if cookie_manager_list is not None:
        for cookie in cookie_manager_list:
            cookie_list.append(cookie)

        if result['city'] not in pd.DataFrame(cookie_manager_list)['city'].values:
            cookie_list.append(result)
    else:
        cookie_list.append(result)

    cookie_manager.set('WeatherCookie', list(cookie_list),
                       expires_at=(datetime.datetime.now() +
                                   datetime.timedelta(minutes=cookie_expiration_time)), key='2')
