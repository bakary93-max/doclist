from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    default_name = "_default"

    @classmethod
    def get_default_collection(cls):
        collection, _ = cls.objects.get_or_create(name="Default", slug=Collection.default_name)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    description = models.TextField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description