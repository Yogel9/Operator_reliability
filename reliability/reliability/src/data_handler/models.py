from django.db import models

class Activity(models.Model):
    """ Деятельность оператора """
    operation = models.CharField('Название операции', max_length=100, unique=True)
    N_count = models.FloatField('Общее число выполненных операций 𝑗-го вида', null=True)
    n_error = models.FloatField('Число ошибок', null=True)
    k = models.FloatField('Число выполненных операций 𝑗-го вида', null=True)
    Pk = models.FloatField('Вероятность выдачи сигнала системой контроля', null=True)
    Pob = models.FloatField('Вероятность обнаружения диспетчером сигнала контроля', null=True)
    Pi = models.FloatField('Вероятность исправления ошибочных действий при повторном выполнении операции', null=True)

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
