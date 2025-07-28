from flask import request, jsonify
from flask_restx import Resource, Namespace
from ..services.search_service import SearchService

hotel_ns = Namespace('hotels', description='Operaciones con hoteles')

@hotel_ns.route('/search')
class HotelSearch(Resource):
    def get(self):
        """Buscar hoteles por ubicación (RF04)"""
        location = request.args.get('location')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        hotels = SearchService.search_hotels(location, start_date, end_date)
        return [{
            'id': hotel.id,
            'name': hotel.name,
            'location': hotel.location,
            'rating': hotel.rating,
            'available_rooms': [{
                'id': room.id,
                'number': room.number,
                'type': room.room_type,
                'price': room.price
            } for room in getattr(hotel, 'available_rooms', [])]
        } for hotel in hotels], 200

@hotel_ns.route('/<int:hotel_id>')
class HotelDetail(Resource):
    def get(self, hotel_id):
        """Detalles de un hotel específico"""
        hotel = SearchService.get_hotel_details(hotel_id)
        if hotel:
            return {
                'id': hotel.id,
                'name': hotel.name,
                'location': hotel.location,
                'description': hotel.description,
                'rating': hotel.rating,
                'rooms': [{
                    'id': room.id,
                    'number': room.number,
                    'type': room.room_type,
                    'price': room.price,
                    'available': room.is_available
                } for room in hotel.rooms]
            }, 200
        return {'message': 'Hotel no encontrado'}, 404