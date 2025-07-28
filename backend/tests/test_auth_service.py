import unittest
from app.services.auth_service import AuthService
from unittest.mock import patch

class TestAuthService(unittest.TestCase):
    
    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_register_user_email_exists(self, mock_get):
        mock_get.return_value = True
        result = AuthService.register_user("Milton", "test@example.com", "1234")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
