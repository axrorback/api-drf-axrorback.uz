from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import MyTokenObtainPairSerializer

class CustomJWTAPI(TokenObtainPairView):
    http_method_names = ['post']
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'access':str(access),
            'refresh':str(refresh),
            'username':user.username,
            'timestamp':datetime.datetime.now(),

        })
