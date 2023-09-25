from django.http import JsonResponse
from django.shortcuts import render

from data_handler.model_service.reliability import get_table_Data, calculation_reliability, delete_Data, update_Data, add_Data


# Create your views here.


def index(request):
    """Страница для работы с таблицей данных"""
    context = {'title': 'Handler',
               'data': get_table_Data(), }
    if request.method == 'POST':
        context['reliability'] = calculation_reliability()
    return render(request, 'table.html', {'context': context, })


def add(request):
    """ Добавление данных """
    return JsonResponse({"status": add_Data(request.POST.dict())})


def delete(request):
    """ Удаление деятельности по id"""
    return JsonResponse({"status": delete_Data(request.POST['id'])})


def update(request):
    """ Редактирование деятельности по id"""
    return JsonResponse({"status": update_Data(request.POST.dict())})
