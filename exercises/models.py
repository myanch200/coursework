from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),

    )
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(default = "exercise-default.jpg")
    video_url = models.URLField(null=True)
    difficulty = models.CharField(max_length=250, null=True, choices=DIFFICULTY_CHOICES)
    content = RichTextField()
    description = models.TextField(null=True)
    image_source = models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.title