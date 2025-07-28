from ..models.hotel import Hotel
from .. import db

class HotelRepository:
    
    @staticmethod
    def create_hotel(name, location, description=None, rating=3.0):
        """Crea nuevo hotel (RF09)"""
        hotel = Hotel(name=name, location=location, 
                     description=description, rating=rating)
        db.session.add(hotel)
        db.session.commit()
        return hotel
    
    @staticmethod
    def update_hotel(hotel_id, **kwargs):
        """Actualiza hotel (RF09)"""
        hotel = Hotel.query.get(hotel_id)
        if not hotel:
            return None
        for key, value in kwargs.items():
            setattr(hotel, key, value)
        db.session.commit()
        return hotel
    
    @staticmethod
    def delete_hotel(hotel_id):
        """Elimina hotel (RF09)"""
        hotel = Hotel.query.get(hotel_id)
        if hotel:
            db.session.delete(hotel)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def search_hotels(location):
        """Busca hoteles por ubicación (RF04)"""
        return Hotel.query.filter(
            Hotel.location.ilike(f'%{location}%')
        ).all()
    
    @staticmethod
    def get_hotel_by_id(hotel_id):
        """Obtiene hotel por ID"""
        return Hotel.query.get(hotel_id)