from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(height_field=200, width_field=200)
    alarm = models.ForeignKey("Alarm", on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Alarm(models.Model):
    time = models.DateTimeField()


class Announcement(models.Model):
    address = models.CharField(max_length=150)
    cost = models.IntegerField()
    square = models.FloatField()
    description = models.TextField(blank=True)
    contacts = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

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