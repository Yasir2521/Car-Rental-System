from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    
class Contact(models.Model):
    time = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=150, default="")
    name = models.CharField(max_length=150, default="")
    message = models.TextField(default="")
    reply = models.TextField(default="")

    def __str__(self):
        return f"{self.name} - {self.reply}"
    
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=30, default="")
    car_color = models.CharField(max_length=30, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'), ('white', 'White')], default='black')
    car_desc = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images", default="")
    manufacturing_date = models.DateField()  # New attribute for manufacturing date
    damages = models.TextField(blank=True, null=True)  # New attribute for damages, optional

    CAR_STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
    ]
    car_status = models.CharField(max_length=20, choices=CAR_STATUS_CHOICES, default='available')
    
    # Choices for the latest safety rating
    SAFETY_RATING_CHOICES = [
        ('Safe for use', 'Safe for use'),
        ('Unfit to drive on roads', 'Unfit to drive on roads'),
    ]
    latest_safety_rating = models.CharField(max_length=50, choices=SAFETY_RATING_CHOICES, default='Safe for use')  # New attribute for latest safety rating

    def __str__(self):
        return f"{self.car_name} - {self.car_id} - {self.car_status}"
    
    
class Order(models.Model) :
    order_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    cars = models.CharField(max_length=50,default="")
    selected_car_id=models.CharField(max_length=50,default="")
    car_color = models.CharField(max_length=30, default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")

    rent_price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Field to store rent price per day
    total_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    payment_status = models.CharField(max_length=20, default="not paid")

    def __str__(self):
        return f"{self.name} - {self.cars}"  
class Review(models.Model):

    name = models.CharField(max_length=20, blank=True)
   
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name        
    

