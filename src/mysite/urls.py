from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # API Document
    # path('schema/', get_schema_view(
    #     title="Dorsa API View",
    #     description="API for sum , total, history",
    #     version="1.0.0"
    # ), name='openapi-schema'),

    # we use spectacular for documenting in api
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name = 'schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
