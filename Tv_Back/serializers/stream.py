from rest_framework import serializers
from Tv_Back.models import Stream


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'
