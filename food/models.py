from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField('음식이름', max_length=20)
    color = models.CharField('색깔', max_length=30)
    value = models.IntegerField('투표')
    