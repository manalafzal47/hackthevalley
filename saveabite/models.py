from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class food_data(models.Model):
    title = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.TextField(max_length=200, default='Unknown', blank=True, null=True)
    stock_status = models.CharField(max_length=200, default='Unknown', blank=True, null=True)
    pickup_or_delivery = models.CharField(max_length=200, default='Unknown', blank=True, null=True)

    def __str__(self):
        return self.name



class user_signup(models.Model):

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

    gov_fname = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    gov_lname = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    phone_number = models.TextField(max=10)
    birthday = models.DateField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = CountryField()
    allergy = models.CharField(max_length=255, choices=ALLERGY_CHOICES, default='none')

    def __str__(self):
        return self.gov_fname
    
    def get_age(self):
        """Calculate the user's age based on the current date."""
        today = timezone.now().date()
        return today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )

    
