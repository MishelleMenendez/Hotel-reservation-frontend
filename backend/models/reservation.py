from . import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending/confirmed/canceled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    
    def confirm(self):
        """Confirma una reserva pendiente"""
        if self.status == 'pending':
            self.status = 'confirmed'
            return True
        return False
    
    def cancel(self):
        """Cancela una reserva"""
        if self.status in ['pending', 'confirmed']:
            self.status = 'canceled'
            return True
        return False
    
    def __repr__(self):
        return f'<Reservation {self.id} - {self.status}>'