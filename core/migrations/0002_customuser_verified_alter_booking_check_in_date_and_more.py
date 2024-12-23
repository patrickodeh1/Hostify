# Generated by Django 5.0.6 on 2024-12-24 06:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(help_text='Start date of the booking.'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(help_text='End date of the booking.'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(help_text='The user who made this booking.', on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='Indicates if the booking is confirmed.'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(help_text='The room that is booked.', on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='core.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, help_text='Total cost of the booking.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='customuser_groups', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.TextField(help_text='Full address of the establishment.'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.CharField(help_text='City where the establishment is located.', max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, help_text='Optional description of the establishment.', null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='Geographical latitude of the establishment.', max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='Geographical longitude of the establishment.', max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(help_text='Name of the hotel or establishment.', max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='owner',
            field=models.OneToOneField(help_text='The owner of this establishment.', on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(help_text='Maximum number of guests allowed in this room.'),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(help_text='The establishment this room belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='core.hotel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_available',
            field=models.BooleanField(default=True, help_text='Indicates if the room is currently available.'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, help_text='Cost per night to book this room.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(help_text='Unique identifier for the room.', max_length=50),
        ),
    ]
