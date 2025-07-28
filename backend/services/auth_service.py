from ..repositories.user_repository import UserRepository
from ..models.user import User
import bcrypt

class AuthService:
    @staticmethod
    def register_user(name, email, password):
        """
        Registra un nuevo usuario (RF01)
        """
        # Verificar si el usuario ya existe
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            return None
        
        # Crear nuevo usuario
        new_user = UserRepository.create_user(name, email, password)
        return new_user

    @staticmethod
    def login_user(email, password):
        """
        Autentica un usuario (RF02)
        """
        return UserRepository.authenticate_user(email, password)

    @staticmethod
    def reset_password(email, new_password):
        """
        Restablece la contraseña de un usuario (RF03)
        """
        user = UserRepository.get_user_by_email(email)
        if not user:
            return False
        return UserRepository.update_password(user.id, new_password)

    @staticmethod
    def get_user_profile(user_id):
        """
        Obtiene el perfil de un usuario
        """
        return User.query.get(user_id)