from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='tstt1@ldkdk.com', password='sddssae'):
    ''' create a sample user '''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with email is successful '''

        email = 'test@test.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        ''' test the email for new user is normalize '''

        email = 'test@CICI.COM'
        user = get_user_model().objects.create_user(email, 'tests2637')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating user with no email raises error'''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        ''' test creating new superuser '''

        user = get_user_model().objects.create_superuser(
            'test2@kdldll.com',
            'testjej738'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        ''' Test the tag string representation '''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )
        self.assertEqual(str(tag), tag.name)
