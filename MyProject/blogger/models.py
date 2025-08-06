from django.db import models

# Create your models here.
class tblbooking(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=60,null=True)
    packagename=models.CharField(max_length=20,null=True)
    pprice=models.FloatField(null=True)
    totalprice=models.FloatField(null=True)
    npeople=models.IntegerField(null=True)
    no_of_days=models.CharField(max_length=50,null=True)
    bookingdatefor=models.CharField(max_length=50,null=True)
    time=models.CharField(max_length=20,null=True)
    booking_date=models.DateField(null=True)
