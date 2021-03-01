from django.db import models

# Create your models here.

class Industry(models.Model):
    name =   models.CharField(max_length=1000)
    description =   models.CharField(max_length=1000)

    def __str__(self):
        return self.id

class Advertiser(models.Model):
    name =   models.CharField(max_length=1000, default=1)
    description =   models.CharField(max_length=1000)
    mobileno =   models.CharField(max_length=10)

    def __str__(self):
        return self.id

class IndustryAdvertiser(models.Model):
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE, null=False)
    advertiser = models.ForeignKey(Advertiser,on_delete=models.CASCADE, null=False)
   

