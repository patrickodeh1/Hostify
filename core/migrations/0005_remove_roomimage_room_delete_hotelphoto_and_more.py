# Generated by Django 5.0.6 on 2025-01-03 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_room_images_room_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomimage',
            name='room',
        ),
        migrations.DeleteModel(
            name='HotelPhoto',
        ),
        migrations.DeleteModel(
            name='RoomImage',
        ),
    ]
