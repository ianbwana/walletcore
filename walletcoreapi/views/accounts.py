from rest_framework import generics, status, response, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import *
from walletcoreapi.serializers.accounts import *
from walletcoreapi.serializers.wallet import *


class ProfileListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class WalletUserListView(generics.ListAPIView):
    '''
    This view returns the details of a test admin.

    Click on the login button on the rest framework console.

    Enter "walletadmin"as username.

    Enter "mobilewallet2020" as password.

    You can also use these credentials to log into the admin console:
    https://walletcore.herokuapp.com/admin/

    You can also navigate to /api/v1/docs/ to view the swagger documentation:
    https://walletcore.herokuapp.com/api/v1/docs/

    Which should show endpoints for the users endpoints.

    If no swagger documentation is on display, click on the session login button to authorize


    '''
    serializer_class = WalletUserSerializer
    queryset = WalletUser.objects.all()[:1]


class WalletUserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletUserSerializer
    queryset = WalletUser.objects.all()


class WalletUserTransactionView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountEntrySerializer

    def get(self, request, userid, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = AccountEntry.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(account__wallet__user__id=self.kwargs["userid"])
        else:
            queryset = AccountEntry.objects.none()
        return queryset


class WalletUserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, userid, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Profile.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(user__id=self.kwargs["userid"])
        else:
            queryset = Profile.objects.none()
        return queryset
