from django.db import models

# Create your models here.




class Customer(models.Model):
     id = models.CharField(max_length=100,primary_key=True)
     name = models.CharField(max_length=100,blank=False)
     dob = models.DateField(auto_now=False, auto_now_add=False)
     updated_on = models.DateTimeField(auto_now=True)

