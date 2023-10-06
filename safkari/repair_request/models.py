from django.db import models
from Operation.models import CustomUser
from Company.models import Branch, Worker
from car_information.models import CarOwner,Car

# Create your models here.
class Repair_Request(models.Model):
    date = models.DateField(auto_now_add=True)
    full_price = models.CharField(max_length=250)
    car_owner_permission = models.BooleanField(default=False)
    km_age = models.IntegerField()
    amount_of_fuel = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    car_owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

class Album(models.Model):
    type = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    repair_request = models.ForeignKey(Repair_Request, on_delete=models.CASCADE)

class Image(models.Model):
    img = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=250)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    description = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    repair_request = models.ForeignKey(Repair_Request, on_delete=models.CASCADE)

class ExtraItems(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    repair_request = models.ForeignKey(Repair_Request, on_delete=models.CASCADE)

class RepairItem(models.Model):
    item_name = models.CharField(max_length=250)
    price = models.IntegerField()
    type = models.CharField(max_length=250)
    time = models.DateTimeField()
    description = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    repair_request = models.ForeignKey(Repair_Request, on_delete=models.CASCADE)

