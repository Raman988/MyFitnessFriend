import django_filters
from .models import *
from django import forms

class fooditemFilter(django_filters.FilterSet):
    # def __init__(self, *args, **kwargs):
    #     super(fooditemFilter, self).__init__(*args, **kwargs)
    #     self.fields['name'].label = ""
    #     self.fields['name'].widget.attrs.update(
    #         {
    #             'placeholder': 'Seach For food',
    #         }
    #     )
    
    class Meta:
        model = Food
        fields = ['name']  