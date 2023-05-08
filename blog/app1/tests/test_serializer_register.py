from django.test import TestCase
from unittest.mock import Mock, patch,call
from app1.serializers.Register import Registerserializer
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializerTestCase(TestCase):

    @patch('django.contrib.auth.models.User.objects.filter')
    def test_validate_username(self, mock_filter):
        mock_query = Mock()
        mock_query.exists.return_value = True
        mock_filter.return_value = mock_query

        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "password123"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        error_message = serializer.errors.get("username")[0]
        self.assertEqual(error_message, 'Username had been taken')

        mock_filter.assert_called_once_with(username='johndoe'.lower())
        mock_query.exists.assert_called_once_with()

    @patch('django.contrib.auth.models.User.objects.filter')
    def test_validate_email(self, mock_filter):
        mock_query = Mock()
        
        def mock_filter_by_email(*args, **kwargs):

            if 'email' in kwargs:
                mock_query.exists.return_value = True
                return mock_query
            else:
                mock_query.exists.return_value = False
                return mock_query
        
        mock_filter.side_effect = mock_filter_by_email


        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "password123"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        error_message = serializer.errors.get('email')[0]
        self.assertEqual(error_message, 'email had been taken')


        mock_filter.assert_has_calls([
            call(email="johndoe@example.com".lower()),
        ])

        

    def test_validate_password(self):
        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "1234567"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        error_message = serializer.errors.get('password')[0]
        self.assertEqual(error_message, 'Password should contain at least 8 characters')

        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "password"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        error_message = serializer.errors.get('password')[0]
        self.assertEqual(error_message, "Password should contain upper letters ")

        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "Password"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        error_message = serializer.errors.get('password')[0]
        self.assertEqual(error_message, 'Password should contain numbers')

        data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "Password123"
        }

        serializer = Registerserializer(data=data)
        serializer.is_valid()

        self.assertFalse(serializer.errors)


