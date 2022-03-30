from django.db import models
from django.contrib.auth.models import User


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
    imagePath = models.CharField(max_length=255)
    cost = models.IntegerField()
    square = models.FloatField()
    floor = models.IntegerField()
    description = models.TextField(blank=True)
    filters = models.ForeignKey("Filters", on_delete=models.CASCADE, blank=True)
    contacts = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.description


class Photo(models.Model):
    photo = models.ImageField(height_field=200, width_field=200)
    announcement = models.ForeignKey("Announcement", on_delete=models.CASCADE)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    message = models.TextField()
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)

class Filters(models.Model):
    appliances = models.ForeignKey("AppliancesFilters", on_delete=models.CASCADE, blank=True)
    house = models.ForeignKey("HouseFilters", on_delete=models.CASCADE, blank=True)

class AppliancesFilters(models.Model):
    fridge = models.BooleanField(blank=True)
    microwave = models.BooleanField(blank=True)
    washMachine = models.BooleanField(blank=True)
    oven = models.BooleanField(blank=True)
    conditioner = models.BooleanField(blank=True)
    router = models.BooleanField(blank=True)
    TV = models.BooleanField(blank=True)

class HouseFilters(models.Model):
    type = models.CharField(max_length=20, blank=True)
    floors = models.IntegerField(blank=True)
    heating = models.CharField(max_length=20, blank=True)


