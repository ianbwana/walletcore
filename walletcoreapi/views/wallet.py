from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet.models import *
from walletcoreapi.serializers.wallet import *


class TransfersListView(generics.ListCreateAPIView):
    """
        To initiate an mpesa transfer send the following to this url

            {

                "amount": 1000,
                "thirdparty": "mpesa",
                "todo": "initiate"

            }
        The customer will get a one time pin.
        You will receive either a status of 200 if the customer has funds
        or a status of 403 if they have no funds or auth failed.

        To complete the transaction send a similar payload but with the otp the customer received:


            {
                "amount": 1000,
                "thirdparty": "mpesa",
                "todo": "complete",
                "otp": 1234

            }

        To initiate a paybill transfer:
            {

                "amount": 1000,
                "thirdparty": "paybill",
                "paybill": 123,
                "todo": "initiate",
                 "account_number": 123

            }

        To complete a paybill transfer:
            {

                "amount": 1000,
                "thirdparty": "paybill",
                "paybill": 123,
                "todo": "complete",
                "otp": 1234,
                "account_number": 123

            }

        To initiate a till number transfer:
            {

                "amount": 1000,
                "thirdparty": "tillnumber",
                "paybill": 123,
                "todo": "initiate",

            }

        To complete a till transfer:
            {

                "amount": 1000,
                "thirdparty": "tillnumber",
                "paybill": 123,
                "todo": "complete",
                "otp": 1234,

            }



        To initiate a bank transaction:
        Send the following payload.

            {
                "amount": 100,
                "thirdparty": "bank",
                "bank_code": "123",
                "bank_name": "abc xyz",
                "bank_account": "012345668",
                "narration": "Transfer to abc bank",
                "todo": "initiate"

            }
        The user will get an expiring otp that you send with the txn.



         To complete the given bank transaction a bank transaction:
         Send the following payload.

            {
                "amount": 100,
                "thirdparty": "bank",
                "bank_code": "123",
                "bank_name": "abc xyz",
                "bank_account": "012345668",
                "narration": "Transfer to abc bank",
                "otp": "567890",
                "todo" "complete"

            }




        """
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()


class AccountsListView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class WalletListView(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()