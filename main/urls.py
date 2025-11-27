from django.urls import path
from main.views import *

urlpatterns = [
    path('question/create/',QuestionCreateAPIView.as_view())
]