from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/',  verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='наименование категории')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_base = models.DateField(null=True, blank=True, verbose_name='дата создания')
    data_change = models.DateField(null=True, blank=True, verbose_name='дата изменения')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                             verbose_name='наименование продукта', related_name='versions')
    version_number = models.IntegerField(verbose_name='версия')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активна')

    def __str__(self):
        return f"{self.product} - {self.version_number}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product', 'version_number',)

    





