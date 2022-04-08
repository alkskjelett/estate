from rest_framework import serializers
from .models import *


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields ='__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    filters = FiltersSerializer()

    class Meta:
        model = Announcement
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'