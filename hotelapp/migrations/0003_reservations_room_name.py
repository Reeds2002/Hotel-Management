# Generated by Django 4.1.3 on 2023-01-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_auto_20230111_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='room_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
