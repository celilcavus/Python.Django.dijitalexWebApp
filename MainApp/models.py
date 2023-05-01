from django.db import models

# Create your models here.
class Home(models.Model):
    Title = models.CharField(max_length=50,null=False)
    SubTitle = models.CharField(max_length=50,null=False)
    Description = models.TextField(max_length=500,null=False,default="")

class AboutUs(models.Model):
    Title = models.CharField(max_length=50,null=False)
    Description = models.TextField(max_length=500,null=False,default="")

class Services(models.Model):
    Icon = models.CharField(max_length=50,null=False)
    Title = models.CharField(max_length=50,null=False)
    Description = models.TextField(max_length=100,null=False,default="")

class ContactUs(models.Model):
    Name = models.CharField(max_length=50,null=False)
    PhoneNumber = models.CharField(max_length=50,null=False,)
    EmailAdress = models.CharField(max_length=50,null=False)
    Message = models.TextField(max_length=50,null=False,default="")
