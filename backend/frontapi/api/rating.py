from rest_framework import serializers
from rest_framework import permissions

from codraw.models.anime import Rating
from codraw.utils.createviews import SetMethodsMetaClass, DependSerializerViewMixin
from codraw.permissions import IsOwnerOrReadOnly


class ReadCreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class UpdateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('value',)


class RatingViewSet(DependSerializerViewMixin, metaclass=SetMethodsMetaClass):
    methods = ('CREATE', 'LIST', 'DETAIL', 'UPDATE')
    queryset = Rating.objects.all()
    read_serializer_class = ReadCreateRatingSerializer
    create_serializer_class = ReadCreateRatingSerializer
    write_serializer_class = UpdateRatingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

