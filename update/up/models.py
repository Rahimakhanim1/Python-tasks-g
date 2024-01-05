from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return self.name
# Create your models here.
