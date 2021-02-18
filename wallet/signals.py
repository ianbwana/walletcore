from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Wallet, Account


@receiver(post_save, sender=Wallet)
def create_user_profile(sender, instance, created=False, **kwargs):
    print("creating account")
    try:
        account_name = "{} {}".format(instance.user.first_name, instance.user.last_name)
        account_description = "An wallet account for" + account_name
        Account.objects.get_or_create(
            name=account_name,
            description=account_description,
            wallet = instance
        )
    except AttributeError:
        print("error")