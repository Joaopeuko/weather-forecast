import streamlit as st


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
