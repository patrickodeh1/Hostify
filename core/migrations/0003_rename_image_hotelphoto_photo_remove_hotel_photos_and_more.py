# Generated by Django 5.0.6 on 2025-01-03 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_hotel_logo_alter_hotel_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelphoto',
            old_name='image',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='photos',
        ),
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(blank=True, help_text='Upload a photo of your hotel', upload_to='hotel_photos/'),
        ),
        migrations.AlterField(
            model_name='hotelphoto',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.hotel'),
        ),
    ]
