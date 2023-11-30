from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey
    price = models.IntegerField()
    date_base = models.DateField(null=True, blank=True, verbose_name='дата создания')
    data_change = models.DateField(null=True, blank=True, verbose_name='дата изменения')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"