from django.urls import path
from main.views import *




urlpatterns = [
    path('question/create/',QuestionCreateAPIView.as_view()),
    path('question/list/',QuestionListAPIView.as_view()),
    path('question/detail/<str:pk>/',QuestionDetailAPIView.as_view()),
    path('contacts/',ContactAPIView.as_view()),
    path('about/',AboutAPIView.as_view()),
    path('achievements/',AchievementsAPIView.as_view()),
    path('gallery/',GalleryAPIView.as_view())
]
