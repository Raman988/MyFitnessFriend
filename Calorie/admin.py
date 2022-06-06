from django.contrib import admin
from .models import Category, Food, Consume, Profile

# Register your models here.
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Consume)
admin.site.register(Profile)
