from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    ingredient = models.CharField(max_length=250)
    nutri_score = models.CharField(max_length=1)
    image = models.URLField()
