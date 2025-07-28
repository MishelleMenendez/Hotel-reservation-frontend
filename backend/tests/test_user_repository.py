import unittest
from flask import Flask
from app.models import db, User
from app.repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase)

    def setUp(self)

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlitememory'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)

        with self.app.app_context()
            db.create_all()

    def tearDown(self)
        with self.app.app_context()
            db.session.remove()
            db.drop_all()

    def test_create_and_get_user_by_email(self)
        with self.app.app_context()
            UserRepository.create_user(Test User, test@example.com, 123456)
            user = UserRepository.get_user_by_email(test@example.com)

            self.assertIsNotNone(user)
            self.assertEqual(user.name, Test User)
            self.assertEqual(user.email, test@example.com)

    def test_authenticate_user_success(self)
        with self.app.app_context()
            UserRepository.create_user(Auth User, auth@example.com, mypassword)
            user = UserRepository.authenticate_user(auth@example.com, mypassword)

            self.assertIsNotNone(user)
            self.assertEqual(user.email, auth@example.com)

    def test_authenticate_user_failure(self)
        with self.app.app_context()
            UserRepository.create_user(Wrong Pass, fail@example.com, rightpass)
            user = UserRepository.authenticate_user(fail@example.com, wrongpass)

            self.assertIsNone(user)

    def test_update_password(self)
        with self.app.app_context()
            user = UserRepository.create_user(Change Pass, change@example.com, oldpass)
            success = UserRepository.update_password(user.id, newpass)
            self.assertTrue(success)

            # Autenticar con nueva contraseña
            updated_user = UserRepository.authenticate_user(change@example.com, newpass)
            self.assertIsNotNone(updated_user)

