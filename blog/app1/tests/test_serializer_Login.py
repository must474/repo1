
from django.test import TestCase
from django.utils.crypto import get_random_string

from ..serializers.Login import Loginserializer


class LoginSerializerTestCase(TestCase):
    def test_serializer_valid_data(self):
        
        username = "user3122"
        password = "121212aA"
        data = {
            "username": username,
            "password": password,
        }
        
        serializer = Loginserializer(data=data)
        
        
        self.assertTrue(serializer.is_valid())
        
        response = serializer.get_tokens_for_user(data)
        self.assertIn("message", response)
        self.assertIn("refresh", response)
        self.assertIn("access", response)
