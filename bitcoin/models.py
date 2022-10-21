from django.db import models



class bitcoin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    coin = models.CharField(max_length=255)
    price=models.FloatField()
    timestamp = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class minmax(models.Model):
    id = models.AutoField(primary_key=True)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)