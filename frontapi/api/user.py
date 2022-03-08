from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from codraw.utils.createviews import SetMethodsMetaClass


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login', 'is_staff', 'password']
        read_only_fields = ['is_staff', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        user = self.context['request'].user
        if data['password']:
            validate_password(data['password'], user=user)
        if data['email']:
            validate_email(data['email'])
        return data


class OneUserViewSet(metaclass=SetMethodsMetaClass):
    methods = ('DETAIL', 'UPDATE', 'DELETE')
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.AllowAny]
    )
    def signup(self, request):
        serializer = AccountSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()



        return Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post'],
        serializer_class=AccountSerializer,
        permission_classes=[permissions.AllowAny]
    )
    def login(self, request):
        pass
