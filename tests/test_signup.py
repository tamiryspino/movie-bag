import unittest
import json

from app import app, api
from database.db import db, initialize_db
from resources.routes import initialize_routes
from tests.BaseCase import BaseCase


class SignupTest(BaseCase):
    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "someone@gmail.com",
            "password": "mycoolpassword"
        })

        # When
        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
