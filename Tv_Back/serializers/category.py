from rest_framework import serializers
from Tv_Back.models import Category, CategoryChannel, CategoryMovie, CategorySerie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryChannel
        fields = '__all__'


class CategoryMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMovie
        fields = '__all__'


class CategorySerieeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySerie
        fields = '__all__'
