
from django.contrib import admin
from django.urls import path , include
from django.http import JsonResponse
import datetime
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(openapi.Info(title="API Documentation", default_version='v1'), public=True)




def notfound(request , exception):
    return JsonResponse({
        "status":False,
        "status_code":404,
        "message":"URL not found or changed!",
        "path":request.path,
        "timestamp":datetime.datetime.now(),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/main/',include('main.urls')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/auth/',include('api.urls')),
    path('api/v1/blog/',include('blog.urls')),
    path('api/v1/restauth/',include('dj_rest_auth.urls'))

]

handler404 = notfound