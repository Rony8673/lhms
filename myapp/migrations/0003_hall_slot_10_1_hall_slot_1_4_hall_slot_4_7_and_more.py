# Generated by Django 5.0.3 on 2024-04-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hall_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='slot_10_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='slot_1_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='slot_4_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='slot_7_10',
            field=models.BooleanField(default=True),
        ),
    ]