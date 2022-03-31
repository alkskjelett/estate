from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/announcement', AnnouncementViewSet, 'announcement')
router.register('api/image', ImageViewSet, 'image')
router.register('api/chat', ChatViewSet, 'chat')
router.register('api/message', MessageViewSet, 'message')
router.register('api/profile', ProfileViewSet, 'profile')
router.register('api/alarm', AlarmViewSet, 'alarm')
router.register('api/filters', FiltersViewSet, 'filters')


urlpatterns = router.urls