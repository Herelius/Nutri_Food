from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    # ingredient = models.CharField(max_length=250)
    nutri_score = models.CharField(max_length=2)
    # image = models.URLField()
