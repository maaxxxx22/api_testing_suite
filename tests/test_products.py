import requests
import json

with open('config/config.json') as config_file:
    config = json.load(config_file)

BASE_URL = config['base_url']

def test_get_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_product():
    headers = {"Authorization": f"Bearer {config['auth_token']}"}
    response = requests.post(f"{BASE_URL}/products", json={
        "name": "Test Product",
        "price": 19.99
    }, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()
