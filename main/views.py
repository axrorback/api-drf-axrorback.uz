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
    http_method_names = ['post']
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
    http_method_names = ['get']
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

class QuestionDetailAPIView(APIView):
    http_method_names = ['get']
    def get(self,request, pk):
        if not pk:
            return Response({
                'status':False,
                'status_code':status.HTTP_400_BAD_REQUEST,
                'message':"ID xato formatda kirtildi!",
                'timestamp':datetime.datetime.now()
            })
        if  not Question.objects.filter(id=pk).exists():
            return Response({
                'status':False,
                'status_code':status.HTTP_404_NOT_FOUND,
                'message':"Bunday ID ga mos savol topilmadi!",
                'timestamp':datetime.datetime.now()
            })
        question = Question.objects.filter(id=pk).first()
        serializer = QuestionDetailSerializer(question)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':'Savol Malumotlari muvaffaqiyatli olindi!',
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })


class ContactAPIView(APIView):
    http_method_names = ['get']
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':"Kontaktlar ro'yxati",
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })


class AboutAPIView(APIView):
    http_method_names = ['get']
    def get(self, request):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':"O'zim haqimda malumotlar",
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })

class AchievementsAPIView(APIView):
    http_method_names = ['get']
    def get(self, request):
        achievements = Achievements.objects.all()
        serializer = AchievementsSerializer(achievements, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':"Muvaffaqiyatlar ro'yxati",
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })

class GalleryAPIView(APIView):
    http_method_names = ['get']
    def get(self, request):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':"Galereya & Rasmlar",
            'data':serializer.data,
            'timestamp':datetime.datetime.now()
        })



