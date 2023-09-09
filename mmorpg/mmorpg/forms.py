from django import forms
from .models import Ad, AdResponse

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'text', 'image', 'category')

class AdResponseForm(forms.ModelForm):
    class Meta:
        model = AdResponse
        fields = ('text',)