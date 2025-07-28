from ..repositories.hotel_repository import HotelRepository
from ..repositories.room_repository import RoomRepository
from datetime import datetime

class SearchService:
    @staticmethod
    def search_hotels(location, start_date=None, end_date=None):
        """
        Busca hoteles por ubicación (RF04)
        """
        hotels = HotelRepository.search_hotels(location)
        
        # Filtrar por disponibilidad si se proporcionan fechas
        if start_date and end_date:
            available_hotels = []
            for hotel in hotels:
                # Verificar disponibilidad de habitaciones
                available_rooms = RoomRepository.find_available_rooms(
                    hotel.id, 
                    datetime.strptime(start_date, '%Y-%m-%d').date(), 
                    datetime.strptime(end_date, '%Y-%m-%d').date()
                )
                if available_rooms:
                    hotel.available_rooms = available_rooms
                    available_hotels.append(hotel)
            return available_hotels
        
        return hotels

    @staticmethod
    def get_hotel_details(hotel_id):
        """
        Obtiene detalles de un hotel específico
        """
        hotel = HotelRepository.get_hotel_by_id(hotel_id)
        if hotel:
            hotel.rooms = RoomRepository.get_rooms_by_hotel(hotel_id)
        return hotel

    @staticmethod
    def get_room_availability(room_id, start_date, end_date):
        """
        Verifica disponibilidad de una habitación (RF05)
        """
        room = RoomRepository.get_room_by_id(room_id)
        if not room:
            return False
        
        return room.check_availability(
            datetime.strptime(start_date, '%Y-%m-%d').date(),
            datetime.strptime(end_date, '%Y-%m-%d').date()
        )