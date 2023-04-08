from django.db import models


class Hotels(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField('Описание', blank=True)
    price_per_day = models.DecimalField('Цена за день', max_digits=7, decimal_places=2)
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class City(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Country(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
