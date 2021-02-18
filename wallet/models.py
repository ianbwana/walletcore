from decimal import Decimal as D
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

from .managers import TransferManager

class Auditable(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    active= models.BooleanField(default=True)

    class Meta:
        abstract=True


class Wallet(Auditable):
    SAVINGS, CURRENT = "savings", "current"
    WALLET_TYPES = [
        ("savings", SAVINGS),
        ("current", CURRENT)
    ]
    name = models.CharField(max_length=124, help_text="A name for this wallet", blank=True)
    description = models.TextField(help_text="A description for this wallet", null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text="Wallet owner",
        blank=True,
        null=True,
        related_name="wallet",
        on_delete=models.PROTECT
    )
    type = models.CharField(choices=WALLET_TYPES, default=CURRENT, max_length=10)
    # To be used for 2 factor authentication. Sends PIN to user email or phone number
    wallet_pin = models.CharField(max_length=128, null=True, blank=True)
    wallet_otp = models.CharField(max_length=128, null=True, blank=True)
    wallet_pin_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    wallet_otp_created = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Account(Auditable):
    name = models.CharField(max_length=100, help_text="A name for this account")
    description = models.TextField(help_text="A brief description of this account")
    wallet = models.OneToOneField(
        "wallet.Wallet",
        help_text="The wallet this account is related to",
        related_name="accounts",
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(
        decimal_places=2, max_digits=12, default=D("0.00"), null=True
    )
    OPEN, FROZEN, CLOSED = "Open", "Frozen", "Closed"
    status = models.CharField(max_length=32, default=OPEN)
    can_be_overdrawn = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Transfer(Auditable):
    message = models.TextField()
    source = models.ForeignKey('wallet.Account', related_name="source_account",on_delete=models.CASCADE)
    destination = models.ForeignKey('wallet.Account', related_name="destination_account",on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="Amount transfered"
    )
    reference = models.CharField(max_length=128, null=True)
    transaction_reversed = models.BooleanField(default=False)

    objects = TransferManager()

    class Meta:
        verbose_name_plural = "Transfers"
        ordering = ["-date_created"]

    def __str__(self):
        return self.message