import os
import pickle

from devices.models import Element
from django.core.files.storage import FileSystemStorage


def SchemSaver(parametrs: dict) -> str:
    """Сохраняем схему в файл"""
    context = {'elements': Element.objects.all(),
               'parametrs': parametrs}

    with open(os.getcwd() + '\\files\\data.pickle', 'wb') as f:
        pickle.dump(context, f)
    return os.getcwd() + '\\files\\data.pickle'


def SchemLoader(file_dir: str) -> dict:
    """Загружаем данные из файла"""
    with open(file_dir, 'rb') as f:
        context = pickle.load(f)

    # Чистим старые элементы
    Element.objects.all().delete()

    # Загружаем новые
    for element in context['elements']:
        element.save()

    return context['parametrs']

