from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from main.serializers import *
from main.models import *
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView, DestroyAPIView, UpdateAPIView



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

class QuestionListAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':'Savollar listi',
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })


# class QuestionDetailAPIView(APIView):
#     def get(self, request, pk=None):
#         if not pk:
#             return Response({
#                 'status':False,
#                 'status_code':status.HTTP_400_BAD_REQUEST,
#                 'message':'Savol idni kiriting!',
#                 'data':None,
#                 'timestamp':datetime.datetime.now()
#             })
#
#         question = Question.objects.filter(id=pk).first()
#         if not question:
#             return Response({
#                 'status':False,
#                 'status_code':status.HTTP_404_NOT_FOUND,
#                 'message':'Savol topilmadi!',
#                 'data':None,
#                 'timestamp':datetime.datetime.now()
#             })
#
#         serializer = QuestionDetailSerializer(question)
#         return Response({
#             'status':True,
#             'status_code':status.HTTP_200_OK,
#             'message':'Savol haqida maʼlumot',
#             'data':serializer.data,
#             'timestamp':datetime.datetime.now()
#         })


class QuestiondDetail(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer