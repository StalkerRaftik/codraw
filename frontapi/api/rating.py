from rest_framework import serializers

from codraw.models.anime import Rating
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerViewMixin
from codraw.permissions import IsOwnerOrReadOnly


class ReadCreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class UpdateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('value',)


class RatingViewSet(DependSerializerViewMixin, metaclass=SetMethodsMetaClass):
    methods = ('CREATE', 'DETAIL', 'UPDATE')
    queryset = Rating.objects.all()
    read_serializer_class = ReadCreateRatingSerializer
    write_serializer_class = UpdateRatingSerializer
    create_serializer_class = ReadCreateRatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
