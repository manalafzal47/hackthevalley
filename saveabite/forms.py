from django import forms
from .models import user_signup

class user_signup(forms.ModelForm):
    class Meta:
        model = user_signup
        fields = ['name', 'birthday', 'allergy']
