from rest_framework import serializers
from accounts.models import *
from wallet.models import Account
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class WalletUserSerializer(serializers.ModelSerializer):
    transactions = serializers.HyperlinkedIdentityField(
        view_name="user-transactions", lookup_url_kwarg="userid")
    balance = serializers.SerializerMethodField()
    # token = serializers.SerializerMethodField()

    def get_balance(self, WalletUser):
        balance = Account.objects.filter(
            wallet__user=WalletUser).values('balance')
        return balance

    # def get_token(self, WalletUser):
    #     token = Profile.objects.filter(user=WalletUser).token
    #     return token

    class Meta:
        model = WalletUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'transactions',
            'balance',
            'password'
        )
