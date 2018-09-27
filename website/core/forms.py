from django import forms
from .models import DataRequest

class DataRequestForm(forms.ModelForm):
    
    class Meta:
        model = DataRequest
        fields = ('name', 'url', 'description')