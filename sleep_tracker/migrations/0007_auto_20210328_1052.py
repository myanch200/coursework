# Generated by Django 3.1.6 on 2021-03-28 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_tracker', '0006_auto_20210328_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 10, 52, 41, 538378)),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 10, 52, 41, 538346)),
        ),
    ]
