from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
