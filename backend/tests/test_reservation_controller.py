import json
from app import create_app
from unittest.mock import patch, MagicMock

app = create_app()
app.testing = True

def test_create_reservation_success():
    with app.test_client() as client, \
         patch('app.services.booking_service.BookingService.create_reservation') as mock_create:
        
        mock_reservation = MagicMock(id=1)
        mock_create.return_value = mock_reservation

        response = client.post('/reservations/', json={
            'user_id': 1,
            'room_id': 101,
            'check_in': '2025-06-01',
            'check_out': '2025-06-05'
        })

        assert response.status_code == 201
        assert response.json['reservation_id'] == 1

def test_cancel_reservation_success():
    with app.test_client() as client, \
         patch('app.services.booking_service.BookingService.cancel_reservation') as mock_cancel:
        
        mock_cancel.return_value = True
        response = client.delete('/reservations/1')

        assert response.status_code == 200
        assert response.json['message'] == 'Reserva cancelada exitosamente'
