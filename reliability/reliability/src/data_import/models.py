from django.db import models

# Create your models here.


class Activity(models.Model):
    """ Деятельность оператора """
    operation = models.CharField('Название операции', max_length=100, unique=True)
    N = models.FloatField('Общее число выполненных операций 𝑗-го вида', max_length=10)
    n = models.FloatField('Число ошибок', max_length=10, null=True)
    k = models.FloatField('Число выполненных операций 𝑗-го вида', max_length=10, null=True)
    Pk = models.FloatField('Вероятность выдачи сигнала системой контроля', max_length=10, null=True)
    Pob = models.FloatField('Вероятность обнаружения диспетчером сигнала контроля', max_length=10, null=True)
    Pi = models.FloatField('Вероятность исправления ошибочных действий при повторном выполнении операции', max_length=10, null=True)

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
