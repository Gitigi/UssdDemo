from django.db import models

class Customer(models.Model):
    phoneNumber = models.CharField(max_length=20)
    balance = models.FloatField(default=0.0)
