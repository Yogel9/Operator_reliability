import os
import pickle

from django.core.files.storage import FileSystemStorage
from survival_analysis.models import Equipment


def SchemSaver(parametrs: dict) -> str:
    """Сохраняем схему в файл"""
    context = {'elements': Equipment.objects.all(),
               'parametrs': parametrs}

    with open(os.getcwd() + '\\files\\data_survive.pickle', 'wb') as f:
        pickle.dump(context, f)
    return os.getcwd() + '\\files\\data_survive.pickle'


def SchemLoader(file_dir: str) -> dict:
    """Загружаем данные из файла"""
    with open(file_dir, 'rb') as f:
        context = pickle.load(f)

    # Чистим старые элементы
    Equipment.objects.all().delete()

    # Загружаем новые
    for element in context['elements']:
        element.save()

    return context['parametrs']

