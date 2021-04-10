from django.db import models

# Create your models here.
class Player(models.Model):
    pno=models.IntegerField()
    pname=models.CharField(max_length=64)
    psal=models.FloatField()
    paddr=models.CharField(max_length=256)
