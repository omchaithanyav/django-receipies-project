from django.db import models


# Create your models here.
class Profile(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=35)
    age = models.IntegerField(default=23)
    email = models.EmailField(null=True)
    address = models.TextField(null=True, blank=True)  

    # refer django models doc for other fields and methods.


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
