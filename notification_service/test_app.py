import unittest
from app import app

class NotificationServiceTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_send_notification(self):
        response = self.client.post('/send_notification', json={
            "name": "Test User",
            "email": "test@example.com"
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
