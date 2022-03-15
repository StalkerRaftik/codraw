from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from codraw.utils.createviews import SetMethodsMetaClass
from codraw.permissions import IsNotAuthenticated


def _user_validator(serializer, data):
    user = serializer.context['request'].user
    if 'password' in data:
        validate_password(data['password'], user=user)
    if 'email' in data:
        validate_email(data['email'])
    return data


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        extra_kwargs = {
            'username': {'write_only': True, 'required': True},
            'password': {'write_only': True, 'required': True},
            'id': {'read_only': True},
        }


class UserCreateSerializer(LoginSerializer):
    class Meta(LoginSerializer.Meta):
        fields = LoginSerializer.Meta.fields + ['email']
        extra_kwargs = {
            **LoginSerializer.Meta.extra_kwargs,
            'email': {'write_only': True, 'required': True},
        }

    validate = _user_validator


class UserRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'last_login', 'is_staff', 'password']
        read_only_fields = ['id', 'is_staff', 'last_login']
        extra_kwargs = {'password': {'write_only': True}}

    validate = _user_validator


class OneUserViewSet(metaclass=SetMethodsMetaClass):
    methods = ('LIST', 'UPDATE', 'DELETE')
    queryset = User.objects.all()
    serializer_class = UserRUDSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(
        detail=False,
        methods=['post'],
        serializer_class=UserCreateSerializer,
        permission_classes=[IsNotAuthenticated],
    )
    def signup(self, request):
        """
        ## Returns only `token` and `id` fields.
        """
        serializer = UserCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        token = Token.objects.create(user=user).pk

        return Response({'token': token}, status=status.HTTP_201_CREATED)

    @action(
        detail=False,
        methods=['post'],
        serializer_class=LoginSerializer,
        permission_classes=[IsNotAuthenticated]
    )
    def login(self, request):
        """
        ## Returns only `token` and `id` fields.
        """
        resp_400 = Response({'error': 'Incorrect login or password!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return resp_400
        if not user.check_password(request.data['password']):
            return resp_400

        token = Token.objects.get_or_create(user=user)[0].pk
        return Response({'token': token}, status=status.HTTP_201_CREATED)
