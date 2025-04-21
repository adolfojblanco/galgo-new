"""
URL configuration for galgo project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.urls import router_user

schema_view = get_schema_view(
   openapi.Info(
      title="GalGo - API Docs",
      default_version='v1',
      description="GalGo, Api docs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hola@adbwebdesign.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/auth/', include('apps.users.urls')),
   path('api/users/', include(router_user.urls)),
   path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
