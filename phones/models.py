from django.db import models


class Phone(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    lte_exists = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    pass
