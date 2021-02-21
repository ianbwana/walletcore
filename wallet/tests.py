from django.test import TestCase
from wallet.models import Wallet, AccountEntry, Account, Transfer
from wallet.seeds.factories import WalletFactory, AccountFactory, TransferFactory, AccountEntryFactory
from accounts.seeds.factories import WalletUserFactory
from django.contrib.auth.models import AnonymousUser
from accounts.models import WalletUser


# Create your tests here.


class WalletModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wallet_user = WalletUser.objects.create(username="johndoe", password="password.123", email="johndoe@mail.com")
        Wallet.objects.create(user=wallet_user, name="John's wallet")

    def test_wallet_has_user(self):
        test_wallet = Wallet.objects.get(id=1)
        self.assertEqual(test_wallet.user.username, 'johndoe')


class AccountModelTestCase(TestCase):
    pass




