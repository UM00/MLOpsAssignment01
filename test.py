import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        app.accuracy = None

    
    def test_model_accuracy_endpoint(self):
        response = self.app.get('/model_accuracy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The model's accuracy is", response.data)

    # def test_model_accuracy_not_available(self):
    # # Set accuracy to None before making the request
    #     app.accuracy = None

    #     response = self.app.get('/model_accuracy')

    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"The model's accuracy is not available.", response.data)


    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    # Add more test cases as needed

    def test_model_accuracy_available(self):
        # Set a mock accuracy value
        app.accuracy = 0.8925
        
        response = self.app.get('/model_accuracy')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The model's accuracy is 0.8925", response.data)


if __name__ == '__main__':
    unittest.main()
