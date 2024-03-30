import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_model_accuracy_endpoint(self):
        response = self.app.get('/model_accuracy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The model's accuracy is", response.data)

    def test_model_accuracy_not_available(self):
        # Clearing accuracy to simulate its unavailability
        app.accuracy = None

        response = self.app.get('/model_accuracy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The model's accuracy is not available.", response.data)

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
