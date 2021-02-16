from django.contrib import admin
from .models import (
    Wallet,
    Account,
    Transfer
)
# Register your models here.
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transfer)