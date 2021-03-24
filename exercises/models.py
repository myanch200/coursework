from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Exercise(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()

    def __str__(self):
        return self.title