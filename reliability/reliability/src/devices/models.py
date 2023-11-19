from django.db import models

# Create your models here.


class Element(models.Model):
    """ Элементы схемы """

    element = models.CharField('Название элемента', max_length=100)
    operating_time = models.FloatField('Наработка(в днях)', null=True)
    date = models.DateField('Дата установки', null=True)
    sub_system = models.FloatField('Номер подсистемы', null=True)
    number = models.FloatField('Номер элемента в системе', null=True)

    class Meta:
        unique_together = ('sub_system', 'number')
        verbose_name = 'Элемент схемы'
        verbose_name_plural = 'Элементы схемы'


class Schem(models.Model):
    """Схема"""
    name = models.CharField('Название схемы', max_length=100)
    type = models.CharField('Тип схемы', max_length=4)
