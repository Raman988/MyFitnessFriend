from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class fooditemForm(ModelForm):
    class Meta:
        model=Food
        fields="__all__"

class addUserFooditem(ModelForm):
    
    class Meta:
        model=Consume
        fields="__all__"
        
class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

class ProfileUpdateForm2(ModelForm):
    class Meta:
        model=Profile
        fields=['calorie_goal']


