import requests
import random
import string
from urls import URL

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_data():
        
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    return courier_data


def register_new_courier_and_return_login_password():
    login_pass = {}

    payload = generate_courier_data()

    response = requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data=payload)
    
    if response.status_code == 201:
        login_pass['login'] = payload['login']
        login_pass['password'] = payload['password']
    
    return login_pass