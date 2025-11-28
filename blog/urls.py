from django.urls import path
from blog.views import *

urlpatterns = [
    path('list/',BlogListAPIView.as_view()),
    path('detail/<str:pk>/',BlogDetailAPIView.as_view())
]