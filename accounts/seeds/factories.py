import factory
from faker import Factory
from accounts.models import WalletUser, Profile

faker = Factory.create()


class WalletUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WalletUser

    username = faker.user_name()
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()


