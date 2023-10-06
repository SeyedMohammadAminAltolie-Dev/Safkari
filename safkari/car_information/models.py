from django.db import models
from Operation.models import CustomUser
# Create your models here.
class CarOwner(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    home_phone_number = models.CharField(max_length=250)
    inviter_name = models.CharField(max_length=250,blank=True)
    description = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.last_name

class Car(models.Model):
    model_name = models.CharField(max_length=250)
    plate = models.CharField(max_length=250)
    chasis_number = models.CharField(max_length=250)
    owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    color = models.CharField(max_length=250)
    operator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)


    def __str__(self):
        return self.model_name + " " + self.plate