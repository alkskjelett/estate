from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.generics import ListAPIView


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnnouncementSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PhotoSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChatSerializer


class ChatViewListVPIView(ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.all()



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer


class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlarmSerializer