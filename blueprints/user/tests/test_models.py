from django.test import TestCase
from rest_framework.authtoken.models import Token

from blueprints.user import models


class UserTestCase(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(email='foo@bar.com', first_name='foo',
                                               last_name='bar', password='fooBar')

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, models.User))

    def test_password_is_encrypted(self):
        self.assertNotEqual(self.user.password, 'fooBar')

    def test_user_creation_creates_cart_instance(self):
        self.assertTrue(self.user.cart_set.count(), 1)

    def test_user_creation_creates_token_instance(self):
        self.assertTrue(Token.objects.count(), 1)
