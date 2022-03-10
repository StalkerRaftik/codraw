from django.urls import path, include
from rest_framework import routers
from frontapi.api.user import OneUserViewSet

router = routers.DefaultRouter()
router.register(r'user', OneUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
