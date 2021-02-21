from django.test import TestCase
from accounts.seeds.factories import WalletUserFactory

# Create your tests here.


class WalletUserTestCase(TestCase):
    def setUp(self):
        self.test_user = WalletUserFactory(
            username="test-username",
            first_name="test-firstname",
            last_name="test-lastname",
            email="tester@mail.com",
            password="password.123"
        )

    def test_wallet_user_model(self):
        new_user = self.test_user
        self.assertEqual(new_user.username, "test-username")
        self.assertEqual(new_user.first_name, "test-firstname")
        self.assertEqual(new_user.last_name, "test-lastname" )
        self.assertEqual(new_user.email, "tester@mail.com" )
        self.assertEqual(new_user.password, "password.123" )