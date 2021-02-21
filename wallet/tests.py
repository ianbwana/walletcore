from django.test import TestCase
from wallet.models import Wallet, AccountEntry, Account, Transfer
from django.contrib.auth import get_user_model

# Create your tests here.


class WalletModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wallet_user = get_user_model().objects.create(
            username="johndoe",
            password="password.123",
            email="johndoe@mail.com"
        )
        Wallet.objects.create(user=wallet_user, name="John's wallet")

    def test_wallet_has_user(self):
        test_wallet = Wallet.objects.get(id=1)
        self.assertEqual(test_wallet.user.username, 'johndoe')


class AccountModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username="johndoe", password="password.123", email="johndoe@mail.com")
        wallet_user = get_user_model().objects.get(id=1)
        Wallet.objects.create(user=wallet_user, name="John's wallet")
        wallet_instance = Wallet.objects.get(id=1)
        Account.objects.create(wallet=wallet_instance, status="Open")

    def test_account_has_wallet(self):
        account = Account.objects.get(id=1)
        self.assertTrue(account.wallet.user.username, "johndoe")

    def test_account_starts_with_zero_balance(self):
        account = Account.objects.get(id=1)
        self.assertEqual(int(account.balance), 0)


class TransferModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username="johndoe", password="password.123", email="johndoe@mail.com")
        get_user_model().objects.create(username="janedoe", password="password.123", email="janedoe@mail.com")
        wallet_user1 = get_user_model().objects.get(id=1)
        wallet_user2 = get_user_model().objects.get(id=1)
        Wallet.objects.create(user=wallet_user1, name="John's wallet")
        Wallet.objects.create(user=wallet_user2, name="John's wallet")
        wallet_instance1 = Wallet.objects.get(id=1)
        wallet_instance2 = Wallet.objects.get(id=2)
        Account.objects.create(wallet=wallet_instance1, status="Open")
        Account.objects.create(wallet=wallet_instance2, status="Open")
        account1 = Account.objects.get(id=1)
        account2 = Account.objects.get(id=2)
        Transfer.objects.create(
            source=account1,
            destination=account2,
            amount=5000,
            message="john to jane")
        Transfer.objects.create(
            source=account2, destination=account1, amount=3000, message="jane to john")

    def test_transfer_has_source_and_destination(self):
        transfer = Transfer.objects.get(id=1)
        self.assertTrue(transfer.source.wallet.user.username, "johndoe")
        self.assertTrue(transfer.destination.wallet.user.username, "janedoe")

    def test_transfer_has_accurate_amount(self):
        transfer = Transfer.objects.get(id=2)
        self.assertEqual(int(transfer.amount), 3000)
        self.assertNotEqual(int(transfer.amount), 300)

    def test_transfer_has_message(self):
        transfer2 = Transfer.objects.get(id=2)
        transfer1 = Transfer.objects.get(id=1)
        self.assertEqual(transfer1.message, "john to jane")
        self.assertNotEqual(transfer2.message, "john to jane")


class AccountEntryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username="johndoe", password="password.123", email="johndoe@mail.com")
        get_user_model().objects.create(username="janedoe", password="password.123", email="janedoe@mail.com")
        wallet_user1 = get_user_model().objects.get(id=1)
        wallet_user2 = get_user_model().objects.get(id=1)
        Wallet.objects.create(user=wallet_user1, name="John's wallet")
        Wallet.objects.create(user=wallet_user2, name="John's wallet")
        wallet_instance1 = Wallet.objects.get(id=1)
        wallet_instance2 = Wallet.objects.get(id=2)
        Account.objects.create(wallet=wallet_instance1, status="Open")
        Account.objects.create(wallet=wallet_instance2, status="Open")
        account1 = Account.objects.get(id=1)
        account2 = Account.objects.get(id=2)
        Transfer.objects.create(
            source=account1,
            destination=account2,
            amount=5000,
            message="john to jane",
            reference="j2j001",
            transaction_type="credit"
        )
        Transfer.objects.create(
            source=account2,
            destination=account1,
            amount=3000,
            message="jane to john",
            reference="j2j002",
            transaction_type="debit"
        )
        transfer1 = Transfer.objects.get(id=1)
        transfer2 = Transfer.objects.get(id=2)

        AccountEntry.objects.create(
            transaction=transfer1,
            account=account1,
            amount=5000
        )
        AccountEntry.objects.create(
            transaction=transfer2,
            account=account2,
            amount=3000
        )

    def test_entry_transaction_has_source(self):
        entry1 = AccountEntry.objects.get(id=1)
        self.assertEqual(entry1.transaction.source.wallet.user.username, "johndoe")

    def test_entry_has_amount(self):
        entry1 = AccountEntry.objects.get(id=1)
        self.assertIn(int(entry1.amount), [5000,-5000])

    def test_entry_transaction_has_type(self):
        entry1 = AccountEntry.objects.get(id=1)
        self.assertEqual(entry1.transaction.transaction_type, "credit")







