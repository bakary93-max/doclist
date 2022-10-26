from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()


class Tasks(models.Model):
    description = models.TextField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)