from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=1000000, default=0)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=1000000)
    size = models.DecimalField(decimal_places=2, max_digits=100000)
    description = models.TextField()
    age_limited =models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
