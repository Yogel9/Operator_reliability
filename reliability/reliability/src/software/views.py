from django.http import JsonResponse
from django.shortcuts import render

from software.models import MillsParam, LipovParam


def info(request):
    """ Информация по модулю """
    context = {'pre_title': 'Info',
               'title': 'Software', }
    return render(request, 'software_index.html', {'context': context, })


def lipov(request):
    """ Модель Липова """
    context = {'pre_title': 'Lipov_model',
               'title': 'Software',
               'parameters': LipovParam.objects.all()}

    return render(request, 'software_lipov.html', {'context': context, })


def mills(request):
    """Модель Миллса"""
    context = {'pre_title': 'Mills_model',
               'title': 'Software',
               'parameters': MillsParam.objects.all()}

    return render(request, 'software_mills.html', {'context': context, })


def add_lipov(request):
    """Добавляем параметры"""
    print(request.POST)
    LipovParam.objects.create(
        HN=request.POST['HN'],
        m=request.POST['m'],
        HS=request.POST['S'],
        n=request.POST['n'],
        HV=request.POST['V'],
    )
    return JsonResponse({"status": "ok"})


def del_lipov(request):
    """Удаляем параметры"""
    LipovParam.objects.get(id=request.POST['id']).delete()
    return JsonResponse({"status": "ok"})


def add_mills(request):
    """Добавляем параметры"""
    MillsParam.objects.create(
        low_n=request.POST['n'],
        high_M=request.POST['M'],
        low_m=request.POST['m'],
    )
    return JsonResponse({"status": "ok"})


def del_mills(request):
    """Удаляем параметры"""
    MillsParam.objects.get(id=request.POST['id']).delete()
    return JsonResponse({"status": "ok"})
