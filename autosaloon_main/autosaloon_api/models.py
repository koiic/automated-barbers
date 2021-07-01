from django.db import models

class Saloon(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

