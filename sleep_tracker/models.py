from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

import pytz 
# Create your models here.
class Sleep(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.now())
    end = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.user.username} - {self.start}/{self.end}'

    
    def calculate_sleep_hours(self):
        duration = (self.end - self.start).total_seconds()
        
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        return f'{hours}:{minutes}'