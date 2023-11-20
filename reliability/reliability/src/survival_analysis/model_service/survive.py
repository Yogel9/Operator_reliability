import datetime
import os
import math

from survival_analysis.models import Equipment


def get_graph_data() -> dict:
    """Получаем параметры для постройки графика """
    data = {'st': list(),
            'dsMax': list(),
            'dsMin': list(),
            't': list(),}
    result = 1
    leftp = 0
    for e in Equipment.objects.all().order_by('time'):
        result = result * function(e.surviving_obj, e.failed_obj)
        # Расчёт доверительного интервала
        leftp = leftp + dsfun(e.surviving_obj, e.failed_obj)
        ds = result * math.sqrt(leftp)
        fa = 0.95
        data['dsMax'].append(result+(fa*ds))
        data['dsMin'].append(result-(fa*ds))
        data['st'].append(result)
        data['t'].append(e.time)
    return data


def dsfun(Y: int, d: int):
    return d/(Y*(Y-d))


def function(Y: int, d: int):
    return (Y - d) / Y
