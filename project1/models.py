from django.db import models
class menu(models.Model):
    nom=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    prix=models.IntegerField(255)
# Create your models here.
