from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.



class Recipe(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, blank=True)
    categories = models.CharField(max_length=120,null=True, blank=True, help_text="Separate categories with ;")
    description = models.TextField(null=True, blank=True)
    prep_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)

    ingredients = models.TextField(null=True, blank=True, help_text="Separate ingredients with ;")
    content = RichTextField(null=True)

    def __str__(self):
        return self.title
class Nutrition(models.Model):
    NUTRITION_CHOICES = (
        ('kcal','Kcal'),
        ('fat','Fat'),
        ('saturates','Saturates'),
        ('carbs','Carbs'),
        ('sugars','Sugars'),
        ('fibre','Fibre'),
        ('salt','Salt'),
        ('protein','Protein'),


    )
    recipe = models.ForeignKey(Recipe, related_name='recipe',on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255,choices=NUTRITION_CHOICES)
    value = models.FloatField(null=True,help_text="In grams")