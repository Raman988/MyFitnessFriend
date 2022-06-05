from django.contrib import admin
from .models import Category, Food, Consume

# Register your models here.
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Consume)
