from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogListAPIView(APIView):
    http_method_names = ['get']
    def get(self, request):
        serializer = BlogSerializer(Blog.objects.all())
        blogs = BlogSerializer(serializer, many=True)
        return Response({
            'status':True,
            'status_code':status.HTTP_200_OK,
            'message':"Bloglar listi",
            'data':blogs.data,
            'timestamp':datetime.datetime.now()
        })



class BlogDetailAPIView(APIView):
    http_method_names = ['get']
    def get(self, request, pk):
        if not pk:
            return Response({
                'status':False,
                'status_code':status.HTTP_400_BAD_REQUEST,
                'message':"ID xato formatda kirtildi!",
                'timestamp':datetime.datetime.now()
            })
        try:
            blog = Blog.objects.get(id=pk)
            serializer = BlogSerializer(blog)
            return Response({
                'status':True,
                'status_code':status.HTTP_200_OK,
                'message':"Blog haqida malumot",
                'data':serializer.data,
                'timestamp':datetime.datetime.now()
            })
        except Blog.DoesNotExist:
            return Response({
                'status':False,
                'status_code':status.HTTP_404_NOT_FOUND,
                'message':"Blog topilmadi!",
                'timestamp':datetime.datetime.now()
            })

