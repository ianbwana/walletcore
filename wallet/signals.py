from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .utils import get_account_balance

from .models import Wallet, Account, Transfer, AccountEntry


@receiver(post_save, sender=Wallet)
def create_user_profile(sender, instance, created=False, **kwargs):
    try:
        account_name = "{} {}".format(
            instance.user.first_name, instance.user.last_name)
        account_description = "An wallet account for" + account_name
        Account.objects.get_or_create(
            name=account_name,
            description=account_description,
            wallet=instance
        )
    except AttributeError:
        print("error")


@receiver(post_save, sender=Transfer)
def create_entries(sender, instance, created=False, **kwargs):
    try:
        if instance.source != instance.destination:
            AccountEntry.objects.create(
                transaction=instance,
                account=instance.source,
                amount=-instance.amount,
                description=instance.message
            )
            AccountEntry.objects.create(
                transaction=instance,
                account=instance.destination,
                amount=instance.amount,
                description=instance.message
            )
        elif instance.source == instance.destination and \
                instance.transaction_type == "credit":
            AccountEntry.objects.create(
                transaction=instance,
                account=instance.source,
                amount=instance.amount,
                description=instance.message
            )
        elif instance.source == instance.destination and \
                instance.transaction_type == "debit":
            AccountEntry.objects.create(
                transaction=instance,
                account=instance.source,
                amount=-instance.amount,
                description=instance.message
            )


    except Exception as e:
        print(e)


@receiver(post_save, sender=AccountEntry)
def update_account_balance(sender, instance, created=False, **kwargs):
    try:
        balance = get_account_balance(instance.account.id)
        Account.objects.filter(
                    wallet__user__id=instance.account.wallet.user.id
                ).update(
                    balance=int(balance)
                )
    except Exception as e:
        print(e)
