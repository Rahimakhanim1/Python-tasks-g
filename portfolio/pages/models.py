from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=20)
    txt1 = models.CharField(max_length=20)
    txt2 = models.CharField(max_length=20)
    img = models.ImageField(upload_to='picture')


class About(models.Model):
    name = models.CharField(max_length=20)
    prof = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now = True)

class Skill(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

# Create your models here.
