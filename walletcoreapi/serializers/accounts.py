from rest_framework import serializers
from accounts.models import *
from wallet.models import Account


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class WalletUserSerializer(serializers.ModelSerializer):
    transactions = serializers.HyperlinkedIdentityField(
        view_name="user-transactions", lookup_url_kwarg="userid")
    balance = serializers.SerializerMethodField()

    def get_balance(self, WalletUser):
        balance = Account.objects.filter(
            wallet__user=WalletUser).values('balance')
        return balance

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
        )
