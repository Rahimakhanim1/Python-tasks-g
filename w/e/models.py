from django.db import models


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]

# class Sinif(models.Model):
#     sagird_adi = models.CharField(max_length = 50)
#     sagird_soyadi = models.CharField(max_length = 50)
#     sagird_yasi = models.IntegerField()
   

#     def __str__(self):
#         return f'{self.sagird_soyadi} {self.sagird_adi}'
    
# class SinifAdres(models.Model):
#     sinifAdres_id = models.OneToOneField(Sinif, on_delete = models.CASCADE)
#     sinif = models.IntegerField()
#     adres = models.CharField(max_length = 100)

#     def __str__(self):
#         return f'{self.sinif} + {self.adres}'
# class father(models.Model):
#     sagird = models.ForeignKey(Sinif,on_delete = models.CASCADE)
#     ad = models.CharField(max_length = 50)

#     def __str__(self):
#         return self.ad
# Create your models here.