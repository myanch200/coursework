# Generated by Django 3.1.6 on 2021-03-28 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0026_auto_20210328_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 13, 4, 57, 592782)),
        ),
    ]
