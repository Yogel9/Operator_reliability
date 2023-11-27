from django.db import models


class MillsParam(models.Model):
    low_n = models.IntegerField('Обнаруженные естественные ошибки n')
    high_M = models.IntegerField('Искусственные ошибки M')
    low_m = models.IntegerField('Обнаруженные искусственные ошибки m')

    class Meta:
        verbose_name = 'Миллс параметр'
        verbose_name_plural = 'Миллс параметры'


class LipovParam(models.Model):
    HN = models.IntegerField('Первоначальное число ошибок в программе N')
    m = models.IntegerField('Количество тестов m')
    HS = models.IntegerField('Количество искусственно внесенных ошибок S')
    n = models.IntegerField('Число найденных собственных ошибок n')
    HV = models.IntegerField('Число обнаруженных к моменту оценки искусственных ошибок V')

    class Meta:
        verbose_name = 'Липов параметр'
        verbose_name_plural = 'Липов параметры'
