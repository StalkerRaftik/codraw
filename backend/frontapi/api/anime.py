from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from codraw.models.anime import Anime, Rating
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerViewMixin
from codraw.permissions import IsStaffOrReadOnly
from .rating import UpdateRatingSerializer, ReadCreateRatingSerializer


class ListAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'name', 'original_name', 'premiere_date', 'image', 'genres', 'raw_rating', 'raw_visits')


class DetailAnimeSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

    def get_user_rating(self, anime):
        user = self.context['request'].user
        if not user.is_authenticated:
            return None

        user_rating = Rating.objects.filter(owner=user, anime=anime).first()
        return getattr(user_rating, 'value', None)


class AnimeViewSet(DependSerializerViewMixin, metaclass=SetMethodsMetaClass):
    queryset = Anime.objects.all()
    read_serializer_class = ListAnimeSerializer
    write_serializer_class = DetailAnimeSerializer
    retrieve_serializer_class = DetailAnimeSerializer
    permission_classes = [IsStaffOrReadOnly]

    @swagger_auto_schema(
        methods=['post'],
        request_body=UpdateRatingSerializer,
        responses={201: ReadCreateRatingSerializer()}
    )
    @action(detail=True, methods=['post'])
    def set_user_rating(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response('Only authenticated users can set rating', status=status.HTTP_403_FORBIDDEN)

        anime = self.get_object()

        serializer = UpdateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_instance, created = Rating.objects.update_or_create(
            anime=anime,
            owner=user,
            defaults={'value': serializer.validated_data['value']}
        )
        status_code = status.HTTP_201_CREATED if created else status.HTTP_204_NO_CONTENT

        return Response(
            ReadCreateRatingSerializer(rating_instance).data,
            status=status_code,
        )
