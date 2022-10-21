from .models import *
from rest_framework import serializers



class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = bitcoin
        fields = '__all__'

class BitcoinSerializer1(serializers.ModelSerializer):
    class Meta:
        model = bitcoin
        fields = ['timestamp','price','coin']

class MinMaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = minmax
        fields = '__all__'