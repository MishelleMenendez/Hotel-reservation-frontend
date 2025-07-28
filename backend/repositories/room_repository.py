from ..models.room import Room
from .. import db
from datetime import date

class RoomRepository:
    
    @staticmethod
    def create_room(hotel_id, number, room_type, price):
        """Crea nueva habitación (RF10)"""
        room = Room(hotel_id=hotel_id, number=number, 
                   room_type=room_type, price=price)
        db.session.add(room)
        db.session.commit()
        return room
    
    @staticmethod
    def update_room(room_id, **kwargs):
        """Actualiza habitación (RF10)"""
        room = Room.query.get(room_id)
        if not room:
            return None
        for key, value in kwargs.items():
            setattr(room, key, value)
        db.session.commit()
        return room
    
    @staticmethod
    def delete_room(room_id):
        """Elimina habitación (RF10)"""
        room = Room.query.get(room_id)
        if room:
            db.session.delete(room)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def find_available_rooms(hotel_id, check_in, check_out):
        """Busca habitaciones disponibles (RF05)"""
        rooms = Room.query.filter_by(hotel_id=hotel_id).all()
        return [
            room for room in rooms
            if room.check_availability(check_in, check_out)
        ]
    
    @staticmethod
    def get_room_by_id(room_id):
        """Obtiene habitación por ID (RF06)"""
        return Room.query.get(room_id)