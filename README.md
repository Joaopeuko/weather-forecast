# Weather Forecast

---

## Table of Content:
   - [About](#about)
   - [Installation](#installation) 
     - [Library explanation]()
   - [How to use](#how-to-use)
     - [Server](#server)
     - [Front end page](#front-end-page)
   - [Test](#test)
   - [License](#license)
   


---
### About:

It is an application that uses server-side and a front end page to display information about the weather
requested by the user.

---

### Installation:
To make everything work properly it is required some python library's, to install it you need to run the code:
```python
pip install -r requirements.txt
```
- #### Library explanation:

In requirements.txt you can find the following library's:
```python
requests
python-dotenv
streamlit
Flask
coverage
```
- requests~=2.26.0

Requests are used to create communication between the front end page and the server.
- python-dotenv~=0.19.1

The library DotEnv is used to hide sensitive information like a public key that is used to retrieve information
from [Open Weather](https://openweathermap.org/current) API.

You need to have a file .env with the information like the one below:

```python
API_KEY = Insert_the_API_key_here
```
- streamlit~=1.0.0

Streamlit is a library used to create the front end of the weather forecast app, it is a library that makes easy 
to create pages.

- Flask~=2.0.2

Flask is used to create the server and cache information.

- coverage

Coverage is used to return a report of the amount of test covered, missed and excluded.

---
### How to use:

To make the weather forecast app work requires two parts, the server, and a front-end page. Both, the server and
the page files need to be running.

- #### Server:

To start the server you need to navigate through the terminal to the folder weather-forecast and type:
```python
python server.py
```

- #### Front end page:

To start the front end page you need to navigate through the terminal to the folder weather-forecast and type:
```python
streamlit run index.py
```

---

### Test
 
To execute the test coverage one needs to navigate inside the test folder and execute the commands below:
```python
coverage run -m server_test  # To run the test
coverage report -m  # To provide the table that can be seen below
coverage html  # To generate the report in HTML
```

| Name              |      Stmts  | Miss | Cover  | Missing |
| :---              |    :----:   |:----:|:----:  |    ---: |
| server_test.py    |       88    |  0   |   100% |         |
| TOTAL             |       88    |  0   |    100%|         |

It is possible to see the HTML report [here](https://htmlpreview.github.io/?https://github.com/Joaopeuko/weather-forecast/blob/master/test/htmlcov/index.html). You can click on server_test.py for more information.

---

### License

[MIT License](https://github.com/Joaopeuko/weather-forecast/blob/master/LICENSE)

---