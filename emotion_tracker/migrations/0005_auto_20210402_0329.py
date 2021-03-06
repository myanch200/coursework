# Generated by Django 3.1.6 on 2021-04-02 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emotion_tracker', '0004_auto_20210402_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diary',
            name='emotion',
            field=models.CharField(choices=[('happy', 'Happy 😄'), ('excited', 'Excited'), ('angry', 'Angry'), ('sad', 'Sad')], default='Unspecified', max_length=300, verbose_name='How do you feel'),
        ),
    ]
