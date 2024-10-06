from django import forms
from .models import user_signup

class user_signup(forms.ModelForm):
    objects = None

    ALLERGY_CHOICES = [
        ('none', 'None'),
        ('peanuts', 'Peanuts'),
        ('shellfish', 'Shellfish'),
        ('dairy', 'Dairy'),
        ('eggs', 'Eggs'),
        ('gluten', 'Gluten'),
        ('soy', 'Soy'),
        ('tree_nuts', 'Tree Nuts'),
        ('wheat', 'Wheat'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    ]

    allergy = forms.ChoiceField(
        choices=ALLERGY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    DIETARY_RESTRICTIONS_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('pescatarian', 'Pescatarian'),
        ('gluten_free', 'Gluten-Free'),
        ('keto', 'Keto'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
    ]

    dietary_restrictions = forms.ChoiceField(
        choices=DIETARY_RESTRICTIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = user_signup
        fields = "__all__"
        labels = {
            'gov_fname', 'Governement First Name',
            'gov_lname', 'Government Last Name',
            'phone_number', 'Phone Number',
            'birthday', 'Birthday',
            'street_address', 'Street Address',
            'city', 'City',
            'state', 'State',
            'zip_code', 'Zip Code',
            'country', 'Country',
            'allergy', 'Allergies',
            'dietary_restrictions', 'Dietary Restrictions'
        }
    