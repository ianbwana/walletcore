from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet.models import *
from walletcoreapi.serializers.wallet import *


class TransfersListView(generics.ListCreateAPIView):
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()


class AccountsListView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class WalletListView(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()