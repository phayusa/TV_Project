from rest_framework import serializers
from Tv_Back.models import Category, CategoryChannel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryChannel
        fields = '__all__'

