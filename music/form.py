from django import forms
from .models import detail
from django.forms import ModelForm



class detailform(ModelForm):
    class Meta:
        model = detail
        fields = '__all__'
       
