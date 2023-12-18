from rest_framework import serializers

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


# from user.models import CustomUser

from  .models import CustomUser

# User =  CustomUser.objects.first()


# token = Token.objects.create(user= User)
# print(token.key)


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'nama_depan', 'nama_belakang', 'image' , 'nomor', 'NIK' ,'Unit')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        # password = make_password(validated_data['password'])
        # user = CustomUser.objects.create(**validated_data)

        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password']),
            nama_depan=validated_data['nama_depan'],
            nama_belakang=validated_data['nama_belakang'],
            # image=validated_data['image'],
            nomor=validated_data['nomor'],
            NIK=validated_data['NIK'],
            Unit=validated_data['Unit'],
        )
    
        user.save()

        # user = CustomUser.objects.create(
        #     username = validated_data['username'],
        #     email=validated_data['email'],
        # )
        return CustomUser(**validated_data)
    

    # def save(self):
    #     username = self.validated_data['username'], 
    #     password = self.validated_data['password'], 
    #     email = self.validated_data['email'], 
    #     nama_depan = self.validated_data['nama_depan'], 
    #     nama_belakang = self.validated_data['nama_belakang'], 
    #     image = self.validated_data['image'] , 
    #     nomor = self.validated_data['nomor'], 
    #     NIK = self.validated_data['NIK'] ,
    #     Unit = self.validated_data['Unit']
