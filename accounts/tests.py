from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='default_user',
                                        email='default@default.default',
                                        password='TesTpaSS1122')
        self.assertEqual(user.username, 'default_user')
        self.assertEqual(user.email, 'default@default.default')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


