from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey
    price = models.IntegerField()
    date_base = models.DateField(null=True, blank=True, verbose_name='дата создания')
    data_change = models.DateField(null=True, blank=True, verbose_name='дата изменения')

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
