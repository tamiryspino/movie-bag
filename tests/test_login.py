import json

from tests.BaseCase import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "someone@gmail.com"
        password = "mycoolpassword"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        # When
        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
