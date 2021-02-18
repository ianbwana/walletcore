
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import WalletUser, Profile
from wallet.models import Wallet


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created=False, **kwargs):
    print("Profile created")
    try:
        wallet_name = "{} {}".format(instance.first_name, instance.last_name)
        wallet_description = "A wallet for " + wallet_name
        Profile.objects.get_or_create(user=instance)
        Wallet.objects.get_or_create(
            user=instance,
            name=wallet_name + " wallet",
            description= wallet_description
        )
    except AttributeError:
        print("error")