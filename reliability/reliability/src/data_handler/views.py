from django.http import JsonResponse
from django.shortcuts import render

from data_handler.model_service.reliability import get_table_Data, calculation_reliability, delete_Data, update_Data, \
    add_Data

from data_handler.model_service.file_handler import file_read, file_save


def info(request):
    """Краткая информация по программному модулю"""
    context = {'pre_title': 'Info',
               'title': 'Operator'}
    return render(request, 'index.html', {'context': context, })


def file(request):
    """Страница для загрузки файлов"""
    context = {'pre_title': 'Import',
               'title': 'Operator'}
    return render(request, 'import.html', {'context': context, })


def index(request):
    """Страница для работы с таблицей данных и расчётами показателей"""
    context = {'pre_title': 'Handler',
               'title': 'Operator',
               'data': get_table_Data(), }
    if request.method == 'POST':
        context['reliability'] = calculation_reliability()
    return render(request, 'table.html', {'context': context, })


def add(request):
    """ API-Добавление данных """
    return JsonResponse({"status": add_Data(request.POST.dict())})


def delete(request):
    """ API-Удаление деятельности по id"""
    return JsonResponse({"status": delete_Data(request.POST['id'])})


def update(request):
    """ API-Редактирование деятельности по id"""
    return JsonResponse({"status": update_Data(request.POST.dict())})


def upload_file(request):
    """ API- загрузка файлов """
    path = file_save(request.FILES['file'])
    file_read(path)
    return JsonResponse({'status': 'okay'})
