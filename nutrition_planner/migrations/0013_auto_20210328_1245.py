# Generated by Django 3.1.6 on 2021-03-28 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0012_auto_20210328_1243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nutrition',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 12, 45, 31, 581490)),
        ),
    ]
