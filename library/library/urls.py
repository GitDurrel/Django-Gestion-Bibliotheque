from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions # Required for drf-yasg
from drf_yasg.views import get_schema_view # Required for drf-yasg
from drf_yasg import openapi # Required for drf-yasg

schema_view = get_schema_view(
   openapi.Info(
      title="API de la Bibliothèque",
      default_version='v1',
      description="Documentation de l'API pour le système de gestion de bibliothèque. "
                  "Fournit des points de terminaison pour gérer les Auteurs, les Livres et les Emprunts.",
      terms_of_service="https://www.example.com/conditions-utilisation",
      contact=openapi.Contact(email="contact@bibliotheque.example.com"),
      license=openapi.License(name="Licence BSD"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authors.urls')),
    path('api/', include('books.urls')),
    path('api/', include('loans.urls')),

    # Swagger / drf-yasg URL patterns
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
