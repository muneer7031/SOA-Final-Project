import unittest
from app import app
from unittest.mock import patch


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch('app.requests.post')  # this mocks notification call
    def test_register(self, mock_post):         
        mock_post.return_value.status_code = 200  # simulate success
        response = self.client.post('/register', json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "test123"
        })
        self.assertEqual(response.status_code, 201)


    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
