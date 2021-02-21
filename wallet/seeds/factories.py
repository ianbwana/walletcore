import factory
from faker import Factory
from wallet.models import Wallet, AccountEntry, Account, Transfer
from accounts.seeds.factories import WalletUserFactory

faker = Factory.create()


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet
    user = factory.RelatedFactory(WalletUserFactory)


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account
        django_get_or_create = ('accounts',)
    wallet = factory.RelatedFactory(WalletFactory)


class TransferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transfer
    source = factory.RelatedFactory(AccountFactory)
    destination = factory.RelatedFactory(AccountFactory)


class AccountEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccountEntry
    name = faker.words()
    transaction = factory.SubFactory(TransferFactory)
    account = factory.SubFactory(AccountFactory)
