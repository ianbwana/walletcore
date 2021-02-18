from django.contrib import admin
from .models import (
    Profile,
    WalletUser
)
# Register your models here.
admin.site.register(Profile)
admin.site.register(WalletUser)
