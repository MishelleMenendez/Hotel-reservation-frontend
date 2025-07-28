from ..models.user import User
from .. import db
import bcrypt

class UserRepository:
    
    @staticmethod
    def create_user(name, email, password):
        """Crea un nuevo usuario (RF01)"""
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_email(email):
        """Obtiene usuario por email (RF02)"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def authenticate_user(email, password):
        """Autentica usuario (RF02)"""
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None
    
    @staticmethod
    def update_password(user_id, new_password):
        """Actualiza contraseña (RF03)"""
        user = User.query.get(user_id)
        if user:
            user.set_password(new_password)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_user_reservations(user_id):
        """Obtiene reservas de un usuario (RF07)"""
        user = User.query.get(user_id)
        return user.reservations if user else []