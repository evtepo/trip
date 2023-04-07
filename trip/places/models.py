from django.db import models


class Hotels(models.Model):
    title = models.CharField('Название', max_length=200)
    content = models.TextField('Описание', blank=True)
    price_per_day = models.DecimalField('Цена за день', max_digits=7, decimal_places=2)
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=200)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
