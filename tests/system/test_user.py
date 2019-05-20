from models.user import UserModel
from tests.base_test import BaseTest
import json

class UserTest(BaseTest):
    def test_user_registration(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data = {'username':'abishaik', 'password':'1234'})

                expected = {'message': 'User created successfully.'}
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('abishaik'))
                self.assertDictEqual(expected, json.loads(response.data.decode('utf-8')))

    def test_register_login(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data = {'username':'abishaik', 'password':'1234'})

                auth_response = client.post('/auth', data = json.dumps({'username':'abishaik', 'password':'1234'}),
                                                    headers = {'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data.decode('utf-8')).keys())

    def test_duplicate_registration(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data = {'username':'abishaik', 'password':'1234'})
                response = client.post('/register', data={'username': 'abishaik', 'password': '1234'})

                expected = {'message': 'The username already exists.'}

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(expected, json.loads(response.data.decode('utf-8')))

