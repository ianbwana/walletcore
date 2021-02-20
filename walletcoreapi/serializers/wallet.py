from rest_framework import serializers
from wallet.models import *


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            'name',
            'description',
            'user',
            'type'
        )


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'active',
            'balance',
            'wallet',
            'status'
        )


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = (
            'message',
            'source',
            'destination',
            'amount',
            'reference',
            'transaction_type'
        )


class AccountEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountEntry
        fields = '__all__'
