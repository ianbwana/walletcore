from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import *
from walletcoreapi.serializers.accounts import *


class ProfileListView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()