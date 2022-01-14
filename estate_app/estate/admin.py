from django.contrib import admin
from .models import *

# Register your models here.


# class AnnouncementAdmin(admin.ModelAdmin):
#     list_display = {'address', 'cost', 'description', 'сontact_details', 'author'}
#     list_display_links = {'address', 'cost'}
#     search_fields = {'address', 'cost'}
#     list_editable = {'address', 'cost', 'descriiption'}
#     list_filter = {'address', 'cost', 'description', 'author'}


# admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Announcement)
admin.site.register(Profile)
admin.site.register(Alarm)
admin.site.register(Photo)
admin.site.register(Chat)
admin.site.register(Message)
