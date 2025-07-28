from ..models.reservation import Reservation
from .. import db
from datetime import datetime

class ReservationRepository:
    
    @staticmethod
    def create_reservation(user_id, room_id, check_in, check_out):
        """Crea nueva reserva (RF06)"""
        reservation = Reservation(
            user_id=user_id,
            room_id=room_id,
            check_in=check_in,
            check_out=check_out
        )
        db.session.add(reservation)
        db.session.commit()
        return reservation
    
    @staticmethod
    def update_reservation(reservation_id, **kwargs):
        """Actualiza reserva (RF08)"""
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return None
        for key, value in kwargs.items():
            setattr(reservation, key, value)
        db.session.commit()
        return reservation
    
    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancela reserva (RF08)"""
        reservation = Reservation.query.get(reservation_id)
        if reservation and reservation.cancel():
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_reservation_by_id(reservation_id):
        """Obtiene reserva por ID (RF07)"""
        return Reservation.query.get(reservation_id)
    
    @staticmethod
    def get_all_reservations():
        """Obtiene todas las reservas (RF11)"""
        return Reservation.query.all()
    
    @staticmethod
    def get_reservations_by_date_range(start_date, end_date):
        """Obtiene reservas en rango de fechas"""
        return Reservation.query.filter(
            Reservation.check_in <= end_date,
            Reservation.check_out >= start_date
        ).all()