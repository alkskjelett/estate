from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.generics import ListAPIView
from .filters import *
from django_filters.rest_framework  import DjangoFilterBackend
from estate import services


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnnouncementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = announcementFilterFields



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer


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


class FiltersViewSet(viewsets.ModelViewSet):
    queryset = Filters.objects.all()
    permisson_choices = [
        permissions.AllowAny
    ]
    serializer_class = FiltersSerializer