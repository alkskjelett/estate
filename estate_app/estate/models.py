from django.db import models
from django.contrib.auth.models import User
from .services import *

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photoPath = models.CharField(max_length=255)
    alarm = models.ForeignKey("Alarm", on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Alarm(models.Model):
    time = models.DateTimeField()


class Announcement(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    cost = models.IntegerField()
    description = models.TextField(blank=True)
    filters = models.ForeignKey("Filters", on_delete=models.CASCADE, blank=True)
    contacts = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    imagePath = models.CharField(max_length=255, blank=True)
    announcement = models.ForeignKey("Announcement", on_delete=models.CASCADE)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    message = models.TextField()
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)


class Filters(models.Model):
    square = models.FloatField(verbose_name='Площадь', blank=True, default=0)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, default=0)
    type = models.IntegerField(verbose_name='Тип дома', choices=HOUSE_TYPES, blank=True, default=0)
    floors = models.IntegerField(verbose_name='Количество этажей', blank=True, default=0)
    heating = models.IntegerField(verbose_name='Вид отопления', choices=HEATING_TYPES, blank=True, default=0)
    fridge = models.BooleanField(verbose_name='Холодильник', default=False)
    microwave = models.BooleanField(verbose_name='Микроволновка', default=False)
    washMachine = models.BooleanField(verbose_name='Стиральная машина', default=False)
    oven = models.BooleanField(verbose_name='Печь', default=False)
    conditioner = models.BooleanField(verbose_name='Кондиционер', default=False)
    router = models.BooleanField(verbose_name='Роутер', default=False)
    TV = models.BooleanField(verbose_name='Телевизор', default=False)

    def __str__(self):
        return str(self.id)