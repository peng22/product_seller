from .models import Product
from .serializers import (UserSerializer,
                        UserLoginSerializer,
                        UserCreateSerializer,
                        PasswordChangeSerializer,
                        ProductSerializer)
from rest_framework import serializers
from rest_framework import generics
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser)
from rest_framework.response import Response
from django_filters import rest_framework as filters

User=get_user_model()

class UserList(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


def login_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password.\
                                             Please try again!")
    return user

def create_user_account(username, email, password,**extra_fields):
    user = get_user_model().objects.create_user(
                        username=username,email=email,
                         password=password,**extra_fields)
    return user


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_classes = {
    'register': UserCreateSerializer,
        'login': UserLoginSerializer,
        'logout':UserLoginSerializer,
        'password_change':PasswordChangeSerializer,

    }
    queryset=User.objects.all()
    @action(methods=['POST', ], detail=False)
    def register(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = UserCreateSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = login_user(**serializer.validated_data)
        data = UserCreateSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)



    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #serializer for each action
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes \
                                     should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()



class ProductViewset(viewsets.ModelViewSet):
    #filter by user
    filterset_fields = ["seller"]
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
