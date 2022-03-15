from django.urls import path, include
from rest_framework import routers
from frontapi.api.user import OneUserViewSet
from frontapi.api.genre import GenreViewSet
from frontapi.api.rating import RatingViewSet
from frontapi.api.anime import AnimeViewSet

router = routers.DefaultRouter()
router.register(r'user', OneUserViewSet)
router.register(r'anime', AnimeViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'rating', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
