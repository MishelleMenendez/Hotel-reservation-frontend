from flask import request, jsonify
from flask_restx import Resource, Namespace
from ..services.auth_service import AuthService

auth_ns = Namespace('auth', description='Operaciones de autenticación')

@auth_ns.route('/register')
class Register(Resource):
    def post(self):
        """Registro de nuevo usuario (RF01)"""
        data = request.get_json()
        user = AuthService.register_user(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )
        if user:
            return {'message': 'Usuario registrado exitosamente', 'user_id': user.id}, 201
        return {'message': 'El email ya está registrado'}, 400

@auth_ns.route('/login')
class Login(Resource):
    def post(self):
        """Autenticación de usuario (RF02)"""
        data = request.get_json()
        user = AuthService.login_user(
            email=data.get('email'),
            password=data.get('password')
        )
        if user:
            return {'message': 'Login exitoso', 'user_id': user.id, 'role': user.role}, 200
        return {'message': 'Credenciales inválidas'}, 401

@auth_ns.route('/reset-password')
class ResetPassword(Resource):
    def post(self):
        """Restablecimiento de contraseña (RF03)"""
        data = request.get_json()
        success = AuthService.reset_password(
            email=data.get('email'),
            new_password=data.get('new_password'))
        if success:
            return {'message': 'Contraseña actualizada exitosamente'}, 200
        return {'message': 'Usuario no encontrado'}, 404