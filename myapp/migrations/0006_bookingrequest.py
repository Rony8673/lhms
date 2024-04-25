# Generated by Django 5.0.3 on 2024-04-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_booking_day_booking_end_time_booking_start_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=20)),
                ('time_slot', models.CharField(max_length=20)),
            ],
        ),
    ]