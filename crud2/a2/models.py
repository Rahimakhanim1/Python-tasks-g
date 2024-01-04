from django.db import models


class Table(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    history = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    img = models.FileField(upload_to = 'images/')

# class Video(models.Model):
#     video = models.FileField(upload_to = 'videos/')

class ERP(models.Model):
    alish = models.IntegerField()
    satish = models.IntegerField()
    miqdar = models.IntegerField()

    def __str__(self):
        return f'{self.alish} {self.satish} {self.miqdar}'

    @property
    def netice(self):
        data = (self.satish - self.alish)*self.miqdar
        return data


class Order(models.Model):
    order_id = models.OneToOneField(Table, on_delete = models.CASCADE,null = True)


    def __str__(self):
        return self.order_id.name
# Create your models here.
