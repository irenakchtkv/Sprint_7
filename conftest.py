import pytest
from generators import generate_courier_data
from API_client import APIClient


@pytest.fixture
def registered_courier():
    courier = generate_courier_data()
    client = APIClient()

    response = client.register_courier(courier)

    assert response.status_code == 201
    
    yield courier

    auth_data = {
                'login': courier['login'],
                'password': courier['password']
    }

    auth_response = client.authorize_courier(auth_data)
    courier_id = auth_response.json()['id']
    client.delete_courier(courier_id)


@pytest.fixture
def courier_cleanup():
    courier = {
        'payload': generate_courier_data(),
        'created': False
    }
    client = APIClient()
    
    yield courier

    if courier['created'] == True:

        auth_data = {
                    'login': courier['payload']['login'],
                    'password': courier['payload']['password']
        }

        auth_response = client.authorize_courier(auth_data)
        courier_id = auth_response.json()['id']
        client.delete_courier(courier_id)