from django.contrib import admin
from .models import (
    Wallet,
    Account,
    Transfer,
AccountEntry
)
# Register your models here.
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(AccountEntry)