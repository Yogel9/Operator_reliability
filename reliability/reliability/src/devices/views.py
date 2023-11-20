import os

import django
from django.core.files.storage import FileSystemStorage
from django.db.backends import sqlite3
from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from devices.models import Element
from devices.model_service.reliability import count_schem

from devices.model_service.file import SchemSaver

from devices.model_service.file import SchemLoader


def info(request):
    """ Информация по модулю """
    context = {'pre_title': 'Info',
               'title': 'Devices', }
    return render(request, 'devices_index.html', {'context': context, })


def scheme(request):
    """ Основная страница для расчета и создания схемы"""
    context = {'pre_title': 'Scheme',
               'title': 'Devices',
               'elements_param': Element.objects.all()}
    if request.method == "POST":
        try:
            Element.objects.create(sub_system=request.POST['sub_system'],
                                   element=request.POST['element'],
                                   number=request.POST['number'],
                                   operating_time=request.POST['operating_time'],
                                   date=request.POST['date'], )
        except django.db.utils.IntegrityError:
            e = Element.objects.get(sub_system=request.POST['sub_system'], number=request.POST['number'])
            e.element = request.POST['element']
            e.operating_time = float(request.POST['operating_time'])
            e.date = request.POST['date']
            e.save()
            print('Замена элемента!')
        print(request.POST)

    return render(request, 'devices_scheme.html', {'context': context, })


def file(request):
    """ Страница для работы с файлами Загрузка/Выгрузка"""
    context = {'pre_title': 'File',
               'title': 'Devices', }
    return render(request, 'devices_index.html', {'context': context, })


def delete(request):
    """ API-Удаление элемента по id"""
    Element.objects.get(id=request.POST['id']).delete()
    return JsonResponse({"status": f'Элемент ID:{request.POST["id"]} удалён'})


def plan(request):
    """ API- Генерация плана по схеме"""
    # print(request.POST)
    open(os.getcwd() + '\\files\\plan.txt', "w")
    count_schem(schem_type=request.POST['type'],
                period=int(request.POST['period']),
                reliability=float(request.POST['reliability'])
                )
    return FileResponse(open(os.getcwd() + '\\files\\plan.txt', 'rb'))


def save_schem(request):
    """ Сохраняем файл со схемой """
    file_dir = SchemSaver(request.POST.dict())
    return FileResponse(open(file_dir, 'rb'))


def load_schem(request):
    """ Загружаем файл из схемы """
    doc = request.FILES['file']
    fs = FileSystemStorage()
    file_name = fs.save(doc.name, doc)
    params = SchemLoader(file_name)
    return JsonResponse(params)
