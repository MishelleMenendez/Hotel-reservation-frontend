from . import db

class Hotel(db.Model):
    __tablename__ = 'hotels'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float, default=3.0)
    
    rooms = db.relationship('Room', backref='hotel', lazy=True)
    
    def __repr__(self):
        return f'<Hotel {self.name}>'