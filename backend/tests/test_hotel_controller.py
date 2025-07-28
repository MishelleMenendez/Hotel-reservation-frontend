import pytest

@pytest.fixture
def client():
    from app import create_app
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_search_hotels(client):
    response = client.get('/hotels/search?location=City&start_date=2025-07-01&end_date=2025-07-05')
    assert response.status_code == 200


def test_get_hotel_details(client):
    # Usamos un ID arbitrario que podría no existir
    response = client.get('/hotels/1')
    assert response.status_code in [200, 404]
