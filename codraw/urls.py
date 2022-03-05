from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

URLS_PATH = f'{settings.PROJECT_NAME}.urls'

schema_view = get_schema_view(
    openapi.Info(
        title="CoDraw API",
        default_version='v1',
    ),
    patterns=[path('api/', include(URLS_PATH)), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path(
        'api/endpoint/',
        TemplateView.as_view(
            template_name=f'swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'
    ),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('api/', include(URLS_PATH)),
]
