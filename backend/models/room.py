from . import db
from datetime import date

class Room(db.Model):
    __tablename__ = 'rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)  # Ej: 'Individual', 'Suite'
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    reservations = db.relationship('Reservation', backref='room', lazy=True)
    
    def check_availability(self, check_in, check_out):
        """Verifica disponibilidad para fechas específicas"""
        overlapping = Reservation.query.filter(
            Reservation.room_id == self.id,
            Reservation.check_in <= check_out,
            Reservation.check_out >= check_in,
            Reservation.status != 'canceled'
        ).first()
        return overlapping is None
    
    def __repr__(self):
        return f'<Room {self.number} - {self.room_type}>'