# Generated by Django 3.1.6 on 2021-03-28 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_tracker', '0041_auto_20210328_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 13, 26, 7, 244335)),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 13, 26, 7, 244303)),
        ),
    ]
