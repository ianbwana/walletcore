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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletUserSerializer
    queryset = WalletUser.objects.all()


class WalletUserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletUserSerializer
    queryset = WalletUser.objects.all()


class WalletUserTransactionView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransferSerializer

    def get(self, request, userid, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Transfer.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(
                destination__wallet__user__id=self.kwargs["userid"]) | queryset.filter(
                source__wallet__user__id=self.kwargs["userid"])
        else:
            queryset = Transfer.objects.none()
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
