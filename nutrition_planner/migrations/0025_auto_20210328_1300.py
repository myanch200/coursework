# Generated by Django 3.1.6 on 2021-03-28 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0024_auto_20210328_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition',
            name='categories',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='cook_time',
            field=models.CharField(default='10 minutes', max_length=100),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 13, 0, 40, 732769)),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='ingredients',
            field=models.TextField(blank=True, help_text='Separate them with ; '),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='prep_time',
            field=models.CharField(default='10 minutes', max_length=100),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 13, 0, 40, 731862)),
        ),
    ]
