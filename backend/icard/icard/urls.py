from django.contrib import admin
from django.urls import path


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="iCard - ApiDoc",
      default_version='v1',
      description="Documentacion iCard",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="barbieri.martin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
