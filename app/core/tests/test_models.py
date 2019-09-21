from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'hello@gmail.com'
        password = 'Hellopass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_use_email_normalize(self):

        email = 'hello@gmail.com'
        user = get_user_model().objects.create_user(email, 'Hellopass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' test creating user with no email raise error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Hellopass123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'hello@gmail.com',
            'Hellopass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
