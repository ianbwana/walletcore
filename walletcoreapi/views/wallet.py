import json
import uuid
from rest_framework import generics, status, permissions, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet.models import *
from accounts.models import *
from wallet.utils import get_account_balance
from wallet.exceptions import *
from walletcoreapi.serializers.wallet import *


class TransfersListView(generics.ListCreateAPIView):
    """
        Return details about a User's transactions
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()


class AccountDetailView(generics.RetrieveUpdateAPIView):
    """
        Return details about a User's account
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class WalletDetailView(generics.RetrieveAPIView):
    """
        Return details about a User's wallet
    """
    serializer_class = WalletSerializer
    queryset = Wallet.objects.prefetch_related("user", "accounts")
    permission_classes = [permissions.IsAuthenticated]


class WalletTransferView(APIView):
    """
        To initiate a funds transfer transfer send a request to this url
        with payload data;
            {
            action: String(Action to be carried out),
            amount: Integer(Amount to be sent),
            source: Integer(representing source ID),
            destination: Integer(representing destination ID),
            message: String(message to send with the transaction
            }
             For Example:

            {
                "action": "tranfer",
                "message: "Here is some money",
                "amount": 1000,
                "source": 5,
                "destination": 6,
                "type": "credit"
            }

            NB: The transaction reference is created automatically on the post method
        """
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if "userid" in self.kwargs and self.kwargs["userid"]:
            user = self.kwargs["userid"]
        if get_account_balance(request.data["source"]) == 0:
            return Response(
                {"message": "Your account does not have a balance"},
                status=status.HTTP_403_FORBIDDEN)

        if request.data["source"] != request.data["destination"] and \
                get_account_balance(request.data["source"]) > 0 and \
                get_account_balance(request.data["source"]) >= request.data["amount"]:

            reference = str(uuid.uuid4()).replace("-", "")
            data = {
                "message": request.data["message"],
                "source": user,
                "destination": request.data["destination"],
                "amount": request.data["amount"],
                "transaction_type": "debit",
                "reference": reference
            }
            serializer = TransferSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, userid, format=None):
        queryset = Transfer.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(
                destination__wallet__user__id=self.kwargs["userid"]) | queryset.filter(
                source__wallet__user__id=self.kwargs["userid"])
        else:
            queryset = Transfer.objects.none()
        qs_serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(qs_serializer.data, status=status.HTTP_200_OK)


class AccountEntryListView(APIView):
    serializer_class = AccountEntrySerializer
    queryset = AccountEntry.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, userid, format=None):
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = self.queryset.filter(
                account__wallet__user__id=self.kwargs["userid"])
        else:
            queryset = AccountEntry.objects.none()
        qs_serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(qs_serializer.data, status=status.HTTP_200_OK)


class AccountDepositWithdrawView(APIView):
    """
        To initiate a funds withdrawal/deposit send a request to this url
        with payload data;
            {
            action: String(Action to be carried out),
            amount: Integer(Amount to be sent),
            source: Integer(representing source ID),
            }

             For Example if depositing:

            {
                "action": "deposit",
                "amount": 1000,
                "source": 5,
            }

            And for withdrawing would be:


            {
                "action": "withdraw",
                "amount": 1000,
                "source": 5,
            }

            NB: The transaction reference, message and type are created automatically on the post method
        """

    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.data['action'] == "withdraw":
            type = "debit"
            message = "Withdrawal of SGD {} from wallet".format(request.data["amount"])
        elif request.data['action'] == "deposit":
            type = "credit"
            message = "Deposit of SGD {} to wallet".format(request.data["amount"])

        reference = str(uuid.uuid4()).replace("-", "")
        data = {
            "message": message,
            "source": request.data["source"],
            "destination": request.data["source"],
            "amount": request.data["amount"],
            "transaction_type": type,
            "reference": reference
        }
        serializer = TransferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, userid, format=None):
        queryset = Transfer.objects.none()
        qs_serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(qs_serializer.data, status=status.HTTP_200_OK)
