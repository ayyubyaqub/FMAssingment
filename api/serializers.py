from rest_framework import serializers
from .models import *

# user registration
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class SignupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            validated_data["password"] = make_password(validated_data.get("password"))
            return super(SignupSerializer, self).create(validated_data)
    class Meta:
            model = User
            fields = ['username','password']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
            model = User
            fields = ['username','password']
# vendor management

class  VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields="__all__"


class  Purchase_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase_order
        fields="__all__"


class  Vendor_performance_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor_performance_History
        fields="__all__"




