from django.db import models

class Test(models.Model):
    ad = models.CharField(max_length=20)
    soyad = models.CharField(max_length=20)

    def __str__(self):
        return self.ad

# Create your models here.
