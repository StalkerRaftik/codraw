from rest_framework import serializers

from codraw.models.anime import Anime
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerViewMixin
from codraw.permissions import IsStaffOrReadOnly


class ListAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'name', 'original_name', 'premiere_date', 'image', 'genres', 'raw_rating', 'raw_visits')


class DetailAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class AnimeViewSet(DependSerializerViewMixin, metaclass=SetMethodsMetaClass):
    queryset = Anime.objects.all()
    read_serializer_class = ListAnimeSerializer
    write_serializer_class = DetailAnimeSerializer
    retrieve_serializer_class = DetailAnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
