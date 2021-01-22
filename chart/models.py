from django.db import models


# Create your models here.

class datas(models.Model):
    number = models.AutoField(primary_key=True)
    value = models.IntegerField(max_length=10, blank=True, null=True)
