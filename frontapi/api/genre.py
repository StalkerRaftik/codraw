from rest_framework import serializers

from codraw.models import Genre
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerMixin
from codraw.permissions import IsStaffOrReadOnly


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class GenreRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreViewSet(DependSerializerMixin, metaclass=SetMethodsMetaClass):
    queryset = Genre.objects.all()
    read_serializer_class = GenreSerializer
    write_serializer_class = GenreSerializer
    retrieve_serializer_class = GenreRetrieveSerializer
    permission_classes = [IsStaffOrReadOnly]
