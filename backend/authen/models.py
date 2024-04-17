from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
class ProfileProgress(models.Model):
    id_progress = models.AutoField(primary_key=True)
    date = models.DateField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    food = models.FloatField()
    medicine = models.FloatField()
    gas = models.FloatField()
    water = models.FloatField()
    mortality = models.FloatField()
    weight = models.FloatField()
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_progress} - {self.date} - {self.id_user}"
