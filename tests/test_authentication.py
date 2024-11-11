import requests
import pytest
import json

with open('config/config.json') as config_file:
    config = json.load(config_file)

BASE_URL = config['base_url']

def test_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_logout():
    headers = {"Authorization": f"Bearer {config['auth_token']}"}
    response = requests.post(f"{BASE_URL}/auth/logout", headers=headers)
    assert response.status_code == 200
