# Generated by Django 4.0.3 on 2022-04-08 21:29

from django.db import migrations, models
import estate.services


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_remove_announcement_floor_remove_announcement_square_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imagePath',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='photoPath',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='aboba', upload_to=estate.services.announcement_directory_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/user/default_avatar', upload_to=estate.services.user_directory_path),
        ),
    ]