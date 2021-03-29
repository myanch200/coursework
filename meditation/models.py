from django.db import models

# Create your models here.
class YogaArticle(models.Model):
    title = models.CharField(max_length=250)
    video_url = models.URLField()
    thumbnail = models.ImageField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title