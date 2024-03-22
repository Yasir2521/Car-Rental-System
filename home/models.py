from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
class Contact(models.Model):
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name
class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images",default="")
    manufacturing_date = models.DateField()  # New attribute for manufacturing date
    damages = models.TextField(blank=True, null=True)  # New attribute for damages, optional
    
    # Choices for the latest safety rating
    SAFETY_RATING_CHOICES = [
        ('Safe for use', 'Safe for use'),
        ('Unfit to drive on roads', 'Unfit to drive on roads'),
    ]
    latest_safety_rating = models.CharField(max_length=50, choices=SAFETY_RATING_CHOICES, default='Safe for use')  # New attribute for latest safety rating


    def __str__(self):
        return self.car_name    
    

