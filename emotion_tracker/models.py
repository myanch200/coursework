from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
# Create your models here.
class Diary(models.Model):
    
    EMOTION_CHOICES =(
            ('happy', 'Happy'),
            ('excited','Excited'),
            ('angry', 'Angry'),
            ('sad', 'Sad')
            )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    emotion = models.CharField(verbose_name="How do you feel" ,max_length=300,choices=EMOTION_CHOICES,blank=False, default='Unspecified')
    comment = models.TextField( null=True)
    date = models.DateField( auto_now_add=True )

    def __str__(self):
        return f'{self.user} - {self.emotion} - {self.date}'