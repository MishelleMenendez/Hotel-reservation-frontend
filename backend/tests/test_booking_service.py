import pytest
from unittest.mock import patch, MagicMock
from app.services.booking_service import BookingService

@patch('app.services.booking_service.RoomRepository')
@patch('app.services.booking_service.ReservationRepository')
@patch('app.services.booking_service.UserRepository')
def test_create_reservation_success(mock_user_repo, mock_res_repo, mock_room_repo):
    mock_room = MagicMock()
    mock_room.check_availability.return_value = True
    mock_room_repo.get_room_by_id.return_value = mock_room

    mock_reservation = MagicMock(id=1)
    mock_res_repo.create_reservation.return_value = mock_reservation

    result = BookingService.create_reservation(1, 101, '2025-06-10', '2025-06-15')
    
    assert result.id == 1
    mock_room_repo.get_room_by_id.assert_called_once()
    mock_res_repo.create_reservation.assert_called_once()

def test_create_reservation_room_unavailable():
    with patch('app.services.booking_service.RoomRepository.get_room_by_id') as mock_get_room:
        mock_room = MagicMock()
        mock_room.check_availability.return_value = False
        mock_get_room.return_value = mock_room

        result = BookingService.create_reservation(1, 101, '2025-06-10', '2025-06-15')
        assert result is None
