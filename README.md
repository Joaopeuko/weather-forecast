# Weather Forecast

---

## Table of Content:
   - [About](#about)
   - [Installation](#installation) 
     - [Library explanation]()
   - [How to use](#how-to-use)
     - [Server](#server)
     - [Front end page](#front-end-page)
   


---
### About:

It is an application that uses server side and a front end page to display information about the weather
requested by the user.

---

### Installation:
To make everything work properly it is required some python library's, to install it you need to run the code:
```python
pip install -r requirements.txt
```
- #### Library explanation:

In requirements.txt you can find this library's:
```python
requests~=2.26.0
python-dotenv~=0.19.1
streamlit~=1.0.0
Flask~=2.0.2
```
- requests~=2.26.0

Requests is used to create the communication between front end page and server.

- python-dotenv~=0.19.1

The library DotEnv is used to hide sensitive information like a public key that is used to retrieved information
from [Open Weather](https://openweathermap.org/current) API.

You need to have a file .env with the information like the one below:

```python
API_KEY = Insert_the_API_key_here
```
- streamlit~=1.0.0

Streamlit is a library used to create the front end of the weather forecast app, it is library that makes easy 
to create pages.

- Flask~=2.0.2

Flask is used to create the server and cach information.

---
### How to use:
To make the weather forecast app work it requires two parts, the server and a front end page. Both, the server and
the page files need to be running.

- #### Server:

To start the server you need to navigate though the terminal to the folder weather-forecast and type:
```python
python server.py
```

- #### Front end page:
To start the front end page you need to navigate though the terminal to the folder weather-forecast and type:
```python
streamlit run index.py
```

---
