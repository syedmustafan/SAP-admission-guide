from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UniRank(models.Model):
    Ranking = models.CharField(max_length=200) 
    uniname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    deps = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)   
    relScore = models.FloatField()    



