from django.db import models

# Create your models here.
class Tour(models.Model):
    # We need a origin country, we need the destination,
    # number of nights, and we need the price for that tour

    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nigths = models.IntegerField()
    price = models.IntegerField()