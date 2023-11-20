from django.db import models


class Equipment(models.Model):
    """ Техническое оборудование """
    time = models.IntegerField('Момент времени')
    surviving_obj = models.IntegerField('Число объектов, доживающих до t')
    failed_obj = models.IntegerField('Число объектов, для которых произошёл исход')
    probability = models.FloatField('Вероятность исхода')

    class Meta:
        verbose_name = 'Техническое оборудование'
        verbose_name_plural = 'Техническое оборудование'
