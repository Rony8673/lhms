# Generated by Django 5.0.3 on 2024-04-06 13:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='day',
            field=models.CharField(default='Monday', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(default='7_10', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='unit',
            field=models.CharField(default='', max_length=100),
        ),
    ]