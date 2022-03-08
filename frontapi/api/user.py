from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from codraw.utils.createviews import SetMethodsMetaClass
from codraw.permissions import IsNotAuthenticated


def base_user_validator(serializer, data):
    user = serializer.context['request'].user
    if data['password']:
        validate_password(data['password'], user=user)
    if data['email']:
        validate_email(data['email'])
    return data


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'password': {'write_only': True},
        }

    validate = base_user_validator


class AuthSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'password': {'write_only': True},
        }

    validate = base_user_validator


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login', 'is_staff', 'password']
        read_only_fields = ['is_staff', 'last_login']
        extra_kwargs = {'password': {'write_only': True}}

    validate = base_user_validator


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
        serializer_class=RegistrationSerializer,
        permission_classes=[IsNotAuthenticated],
    )
    def signup(self, request):
        """
        ## Returns only `token` field.
        """
        serializer = RegistrationSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user).pk

        return Response({'token': token}, status=status.HTTP_201_CREATED)

    @action(
        detail=False,
        methods=['post'],
        serializer_class=AuthSerializer,
        permission_classes=[IsNotAuthenticated]
    )
    def login(self, request):
        """
        ## Returns only `token` field.
        """
        user = User.objects.get(username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'error': 'Incorrect password!'}, status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.get_or_create(user=user)[0].pk
        return Response({'token': token}, status=status.HTTP_201_CREATED)
