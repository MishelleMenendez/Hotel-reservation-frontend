from flask import request, jsonify
from flask_restx import Resource, Namespace
from ..services.booking_service import BookingService
from datetime import datetime

reservation_ns = Namespace('reservations', description='Operaciones con reservas')

@reservation_ns.route('/')
class ReservationList(Resource):
    def get(self):
        """Obtener reservas del usuario (RF07)"""
        # En producción, obtener user_id del token JWT
        user_id = request.args.get('user_id', 1)  
        reservations = BookingService.get_user_reservations(user_id)
        return [{
            'id': r.id,
            'check_in': r.check_in.isoformat(),
            'check_out': r.check_out.isoformat(),
            'status': r.status,
            'room_id': r.room_id,
            'created_at': r.created_at.isoformat()
        } for r in reservations], 200

    def post(self):
        """Crear nueva reserva (RF06)"""
        data = request.get_json()
        reservation = BookingService.create_reservation(
            user_id=data.get('user_id', 1),  # Obtener de autenticación
            room_id=data['room_id'],
            check_in=datetime.fromisoformat(data['check_in']),
            check_out=datetime.fromisoformat(data['check_out'])
        )
        if reservation:
            return {
                'message': 'Reserva creada exitosamente',
                'reservation_id': reservation.id
            }, 201
        return {'message': 'Habitación no disponible para las fechas seleccionadas'}, 400

@reservation_ns.route('/<int:reservation_id>')
class ReservationDetail(Resource):
    def put(self, reservation_id):
        """Modificar reserva (RF08)"""
        data = request.get_json()
        updates = {}
        if 'check_in' in data:
            updates['check_in'] = datetime.fromisoformat(data['check_in'])
        if 'check_out' in data:
            updates['check_out'] = datetime.fromisoformat(data['check_out'])
        
        reservation = BookingService.update_reservation(reservation_id, **updates)
        if reservation:
            return {
                'message': 'Reserva actualizada',
                'reservation_id': reservation.id
            }, 200
        return {'message': 'Reserva no encontrada'}, 404

    def delete(self, reservation_id):
        """Cancelar reserva (RF08)"""
        success = BookingService.cancel_reservation(reservation_id)
        if success:
            return {'message': 'Reserva cancelada exitosamente'}, 200
        return {'message': 'Reserva no encontrada o ya cancelada'}, 404