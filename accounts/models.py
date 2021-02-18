from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
# Create your models here.


class WalletUser(AbstractUser):
    pass

    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    MALE = 'male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    EIGHTEEN_TWENTY_FOUR = "18-24"
    TWENTY_FIVE_THIRTY_FOUR = "25-34"
    THIRTY_FIVE_FORTY_FOUR = "35-44"
    FORTY_FIVE_FIFTY_FOUR = "45-54"
    FIFTY_FIVE_SIXTY_FOUR = "55-64"
    ABOVE_SIXTY_FIVE = "65+"

    AGE_RANGES = (
        (EIGHTEEN_TWENTY_FOUR, _("Eighteen to twenty four")),
        (TWENTY_FIVE_THIRTY_FOUR, _("Twenty five to thirty four")),
        (THIRTY_FIVE_FORTY_FOUR, _("Thirty five to forty four")),
        (FORTY_FIVE_FIFTY_FOUR, _("Forty five to fifty four")),
        (FIFTY_FIVE_SIXTY_FOUR, _("Fifty five to sixty four")),
        (ABOVE_SIXTY_FIVE, _("Above sixty five")),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    age = models.CharField(choices=AGE_RANGES, max_length=8, null=True, blank=True)


    def __str__(self):
        return self.user.first_name + self.user.last_name

    @property
    def token(self):
        token, _ = Token.objects.get_or_create(user=self.user)
        return token.key

