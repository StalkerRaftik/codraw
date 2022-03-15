from rest_framework import serializers

from codraw.models.anime import Anime
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerMixin
from codraw.permissions import IsStaffOrReadOnly


from django.core.management import call_command

# call_command('loadcsv', 'animes.csv')


class ListAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'name', 'image')


class DetailAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class AnimeViewSet(DependSerializerMixin, metaclass=SetMethodsMetaClass):
    queryset = Anime.objects.all()
    read_serializer_class = ListAnimeSerializer
    write_serializer_class = DetailAnimeSerializer
    retrieve_serializer_class = DetailAnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
