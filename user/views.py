# from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserRegisterSerializer

# from django.contrib.auth import get_user_model

# class UserLoginView(ObtainAuthToken):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user_id': user.pk, 'username': user.username}, status=status.HTTP_200_OK)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        myCourse = [
            {"id_course" : 1,"judul" : "Kursus MySql"},
            {"id_course" : 2,"judul" : "Kursus MongoDB"}
        ]

        token = super().get_token(user)

        token['user'] = { "username" : user.username , "email" : user.email , "myCourses" : myCourse}

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token'
#     ]

#     return Response(routes)