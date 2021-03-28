from django.contrib import admin
from .models import Recipe,Nutrition


class NutritionInline(admin.StackedInline):
    model = Nutrition
    extra = 1

class AdminRecipe(admin.ModelAdmin):
    fieldsets = [
        ('Headlines',               {'fields': ['title','thumbnail']}),
        ('Main', {'fields': ['content','description','ingredients']}),
        ('Additional', {'fields': ['prep_time','cook_time','servings','categories']}),

    ]
    inlines = [NutritionInline]
admin.site.register(Recipe,AdminRecipe)

