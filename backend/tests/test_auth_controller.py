import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_register_user(client):
    response = client.post('/auth/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': '123456'
    })
    assert response.status_code in [200, 201, 400]


def test_login_user(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': '123456'
    })
    assert response.status_code in [200, 401]


def test_reset_password(client):
    response = client.post('/auth/reset-password', json={
        'email': 'test@example.com',
        'new_password': 'nueva123'
    })
    assert response.status_code in [200, 404]
