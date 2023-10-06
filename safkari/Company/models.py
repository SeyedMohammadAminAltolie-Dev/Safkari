from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    owner_name = models.CharField(max_length=250)
    owner_phone_number = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.last_name