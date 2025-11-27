from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from main.serializers import *
from main.models import *




class QuestionCreateAPIView(APIView):
    def get(self, request):
        return Response({
            'status':False,
            'status_code':status.HTTP_405_METHOD_NOT_ALLOWED,
            'message':'GET method uchun ruhsat berilmagan!',
            'data':None,
            'timestamp':datetime.datetime.now()
        })
    def post(self, request):
        serializer = QuestionFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status':True,
                'status_code':status.HTTP_201_CREATED,
                'message':"Savol muvaffaqiyatli jo'natildi! Admin Javobini kuting!",
                'timestamp':datetime.datetime.now()
            })