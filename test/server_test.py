import requests
import pytest

SERVER_URL = 'http://127.0.0.1:5000'

# All the functions below try to anticipate the problems that might appear when using the
# two functions that call the server.

# City Name ---
#   - Title String
#   - Upper String
#   - Lower String
#   - With accent String
#   - With special Character (?%$#*()-) String
#   - Number
#   - Valid String Plus Number
#   - Empty
#   - Character

def test_result_number_title_string():
    result = requests.get(f'{SERVER_URL}/weather/{"London"}')
    assert result.status_code == 200


def test_result_number_upper_string():
    result = requests.get(f'{SERVER_URL}/weather/{"LONDON"}')
    assert result.status_code == 200


def test_result_number_lower_string():
    result = requests.get(f'{SERVER_URL}/weather/{"london"}')
    assert result.status_code == 200


def test_result_number_accent_string():
    result = requests.get(f'{SERVER_URL}/weather/{"lóndón"}')
    assert result.status_code == 404


def test_result_number_special_character_before_string():
    result = requests.get(f'{SERVER_URL}/weather/{"?!#london"}')
    assert result.status_code == 404


def test_result_number_special_character_after_string():
    result = requests.get(f'{SERVER_URL}/weather/{"london!#"}')
    assert result.status_code == 404


def test_result_number_number_string():
    result = requests.get(f'{SERVER_URL}/weather/{"1234"}')
    assert result.status_code == 404


def test_result_number_string_plus_number_after_string():
    result = requests.get(f'{SERVER_URL}/weather/{"london1234"}')
    assert result.status_code == 404


def test_result_number_string_plus_number_before_string():
    result = requests.get(f'{SERVER_URL}/weather/{"1234london"}')
    assert result.status_code == 404


def test_result_number_empty_string():
    result = requests.get(f'{SERVER_URL}/weather/{""}')
    assert result.status_code == 404


def test_result_number_character_string():
    result = requests.get(f'{SERVER_URL}/weather/{"a"}')
    assert result.status_code == 404


# Max Number ---
#   - Integer number - ok
#   - Float number
#   - Negative number
#   - Character
#   - String - ok
#   - Empty - ok
#   - Zero

def test_max_number_number_integer_number():
    result = requests.get(f'{SERVER_URL}/weather?max={3}')
    assert result.status_code == 200


def test_max_number_number_zero_number():
    result = requests.get(f'{SERVER_URL}/weather?max={0}')
    assert result.status_code == 200


def test_max_number_number_negative_number():
    result = requests.get(f'{SERVER_URL}/weather?max={-5}')
    assert result.status_code == 200


def test_max_number_number_float_number():
    result = requests.get(f'{SERVER_URL}/weather?max={1.23}')
    assert result.status_code == 200


def test_max_number_number_missing_number():
    assert requests.get(f'{SERVER_URL}/weather?max=').status_code == 200


def test_max_number_number_return_type():
    assert type(requests.get(f'{SERVER_URL}/weather?max=').json()) == type(list())


def test_max_number_number_missing_character():
    assert requests.get(f'{SERVER_URL}/weather?max').status_code == 200


def test_max_number_number_missing_wrong_input():
    assert requests.get(f'{SERVER_URL}/weather?ma').status_code == 200


def test_max_number_number_missing_wrong_input_2():
    assert requests.get(f'{SERVER_URL}/weather?m').status_code == 200


def test_max_number_number_missing_wrong_input_valid():
    assert requests.get(f'{SERVER_URL}/weather?wrong_name').status_code == 200


def test_max_number_number_short_input():
    assert requests.get(f'{SERVER_URL}/weather?').status_code == 200


def test_max_number_number_short_input_2():
    assert requests.get(f'{SERVER_URL}/weather').status_code == 200


if __name__ == '__main__':
    # Run the server to be able to test the functions.

    # # City name:
    test_result_number_title_string()
    test_result_number_upper_string()
    test_result_number_lower_string()
    test_result_number_accent_string()
    test_result_number_special_character_before_string()
    test_result_number_special_character_after_string()
    test_result_number_number_string()
    test_result_number_string_plus_number_after_string()
    test_result_number_string_plus_number_before_string()
    test_result_number_empty_string()
    test_result_number_character_string()

    # -----
    # Max Number:
    test_max_number_number_integer_number()
    test_max_number_number_zero_number()
    test_max_number_number_negative_number()
    test_max_number_number_float_number()
    test_max_number_number_missing_number()
    test_max_number_number_return_type()
    test_max_number_number_missing_character()
    test_max_number_number_missing_wrong_input()
    test_max_number_number_missing_wrong_input_2()
    test_max_number_number_missing_wrong_input_valid()
    test_max_number_number_short_input()
    test_max_number_number_short_input_2()
