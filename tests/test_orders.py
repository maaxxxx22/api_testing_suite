import requests
import json

with open('config/config.json') as config_file:
    config = json.load(config_file)

BASE_URL = config['base_url']

def test_place_order():
    headers = {"Authorization": f"Bearer {config['auth_token']}"}
    response = requests.post(f"{BASE_URL}/orders", json={
        "product_id": 1,
        "quantity": 2
    }, headers=headers)
    assert response.status_code == 201
    assert "order_id" in response.json()

def test_get_orders():
    headers = {"Authorization": f"Bearer {config['auth_token']}"}
    response = requests.get(f"{BASE_URL}/orders", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
