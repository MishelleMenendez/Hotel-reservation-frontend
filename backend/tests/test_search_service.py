import pytest
from unittest.mock import patch, MagicMock
from app.services.search_service import SearchService

@patch('app.services.search_service.HotelRepository')
@patch('app.services.search_service.RoomRepository')
def test_search_hotels_with_availability(mock_room_repo, mock_hotel_repo):
    hotel = MagicMock(id=1, name='Hotel Uno', location='Lima')
    mock_hotel_repo.search_hotels.return_value = [hotel]

    mock_room_repo.find_available_rooms.return_value = [MagicMock(id=101)]
    
    result = SearchService.search_hotels('Lima', '2025-06-01', '2025-06-05')
    assert len(result) == 1
    assert hasattr(result[0], 'available_rooms')
    assert result[0].available_rooms[0].id == 101

def test_get_hotel_details_with_rooms():
    with patch('app.services.search_service.HotelRepository.get_hotel_by_id') as mock_get_hotel, \
         patch('app.services.search_service.RoomRepository.get_rooms_by_hotel') as mock_get_rooms:
        hotel = MagicMock(id=1, name='Hotel Uno')
        mock_get_hotel.return_value = hotel
        mock_get_rooms.return_value = [MagicMock(id=1, number=101)]
        
        result = SearchService.get_hotel_details(1)
        assert result.rooms[0].number == 101
