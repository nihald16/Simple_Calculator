from django.db import models
from django.db.models.fields import BooleanField
from phonenumber_field.modelfields import PhoneNumberField


GENDERS= (
    ('U','Undefined'),
    ('F','Female'),
    ('M','Male')
)
# Create your models here.
class firstdb(models.Model):
    Username=models.CharField(max_length=100)
    Email=models.EmailField()
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Phone_no=PhoneNumberField()
    Address=models.TextField()
    Password=models.CharField(max_length=100)
    Confirm_Pass=models.CharField(max_length=100)
    Gender=models.CharField(choices=GENDERS,max_length=2)
    DOB=models.DateField()
    over_18=BooleanField()