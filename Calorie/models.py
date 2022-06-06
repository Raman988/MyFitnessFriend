from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    options=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks'),
    )
    name=models.CharField(max_length=50,choices=options)
    def __str__(self):
        return self.name

class Food(models.Model):

   
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
    def __str__(self):
        return str(self.name)
      
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/dept-4.jpg"



class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)



class Profile(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    calorie_goal = models.FloatField(default="2000")


