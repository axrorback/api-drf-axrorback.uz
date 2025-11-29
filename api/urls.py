from django.urls import path
from .views import CustomJWTAPI
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', CustomJWTAPI.as_view(),),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]