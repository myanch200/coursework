# Generated by Django 3.1.6 on 2021-03-28 11:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0015_auto_20210328_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 12, 49, 3, 822972)),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition_planner.recipe')),
            ],
        ),
    ]
