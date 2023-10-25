from data_handler.models import Activity
from statistics import mean

from django.db.models import QuerySet


def add_Data(data) -> str:
    """ Добавление деятельности"""
    obj = Activity.objects.get_or_create(operation=data['operation'])
    obj[0].N_count = data['N_count']
    obj[0].n_error = data['n_error']
    obj[0].k = data['k']
    obj[0].Pk = data['Pk']
    obj[0].Pob = data['Pob']
    obj[0].Pi = data['Pi']
    obj[0].save()
    return f'Элемент ID:{obj[0].id} добавлен!'


def get_table_Data() -> QuerySet:
    """ Получить все записи из таблицы модели Activity"""
    return Activity.objects.all()


def delete_Data(id: int) -> str:
    """ Удалить деятельность по id"""
    try:
        Activity.objects.get(id=id).delete()
        return f'Деятельности с ID:{id} удален!'
    except Activity.DoesNotExist:
        return f'Деятельности с ID:{id} не существует!'


def update_Data(data: dict) -> str:
    """ Редактировать деятельность по id"""
    try:
        obj = Activity.objects.get(id=data['id'])
        obj.operation = data['operation']
        obj.N_count = data['N_count']
        obj.n_error = data['n_error']
        obj.k = data['k']
        obj.Pk = data['Pk']
        obj.Pob = data['Pob']
        obj.Pi = data['Pi']
        obj.save()
        return f'Деятельности с ID:{id} изменена!'
    except Activity.DoesNotExist:
        return F'Деятельности с ID:{id} не существует!'


def calculation_reliability() -> tuple:
    """ Расчет параметров надежности оператора """
    Pisp_list = list()
    Pop = 1
    for item in Activity.objects.all():
        Pisp_list.append(item.Pk * item.Pob * item.Pi)
        Pop = Pop * ((item.N_count - item.n_error) / item.N_count) ** item.k
    Pisp = mean(Pisp_list)
    Pd = Pop + (1 - Pop) * Pisp
    return round(Pd, 3), round(Pop, 3), round(Pisp, 3)
