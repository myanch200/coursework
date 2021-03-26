from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz 
# Create your models here.
class Sleep(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.start}/{self.end}'

    
    def calculate_sleep_hours(self):
        return self.end - self.start