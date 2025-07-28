from ..repositories.reservation_repository import ReservationRepository
from ..repositories.room_repository import RoomRepository
from ..repositories.user_repository import UserRepository
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class BookingService:
    @staticmethod
    def create_reservation(user_id, room_id, check_in, check_out):
        """
        Crea una nueva reserva (RF06, RF12)
        """
        # Verificar disponibilidad
        room = RoomRepository.get_room_by_id(room_id)
        if not room or not room.check_availability(check_in, check_out):
            return None
        
        # Crear reserva
        reservation = ReservationRepository.create_reservation(
            user_id, room_id, check_in, check_out
        )
        
        # Enviar confirmación por correo
        BookingService.send_confirmation_email(reservation.id)
        return reservation

    @staticmethod
    def get_user_reservations(user_id):
        """
        Obtiene reservas de un usuario (RF07)
        """
        return ReservationRepository.get_reservations_by_user(user_id)

    @staticmethod
    def update_reservation(reservation_id, **kwargs):
        """
        Actualiza una reserva (RF08, RF13)
        """
        reservation = ReservationRepository.update_reservation(reservation_id, **kwargs)
        if reservation and 'status' in kwargs:
            BookingService.send_notification_email(reservation.id, kwargs['status'])
        return reservation

    @staticmethod
    def cancel_reservation(reservation_id):
        """
        Cancela una reserva (RF08, RF13)
        """
        success = ReservationRepository.cancel_reservation(reservation_id)
        if success:
            BookingService.send_notification_email(reservation_id, 'canceled')
        return success

    @staticmethod
    def send_confirmation_email(reservation_id):
        """
        Envía correo de confirmación (RF12)
        """
        reservation = ReservationRepository.get_reservation_by_id(reservation_id)
        if not reservation:
            return False
        
        user = UserRepository.get_user_by_id(reservation.user_id)
        subject = "Confirmación de Reserva"
        body = f"Hola {user.name},\n\nTu reserva #{reservation_id} ha sido confirmada."
        return BookingService._send_email(user.email, subject, body)

    @staticmethod
    def send_notification_email(reservation_id, action):
        """
        Envía notificación por correo (RF13)
        """
        reservation = ReservationRepository.get_reservation_by_id(reservation_id)
        if not reservation:
            return False
        
        user = UserRepository.get_user_by_id(reservation.user_id)
        subject = f"Reserva {action.capitalize()}"
        body = f"Hola {user.name},\n\nTu reserva #{reservation_id} ha sido {action}."
        return BookingService._send_email(user.email, subject, body)

    @staticmethod
    def _send_email(to, subject, body):
        """
        Método auxiliar para enviar correos
        """
        # Configuración de correo (debería estar en config.py)
        sender = "no-reply@hotelapp.com"
        
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = to
            
            # En un entorno real, usar servidor SMTP real
            # with smtplib.SMTP('smtp.server.com') as server:
            #     server.sendmail(sender, [to], msg.as_string())
            print(f"Email enviado a {to}: {subject}")
            return True
        except Exception as e:
            print(f"Error enviando email: {e}")
            return False