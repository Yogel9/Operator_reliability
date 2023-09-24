import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse

from data_import.model_service.file_handler import file_save, file_read


# Create your views here.


def index(request):
    """Страница для загрузки файлов"""
    context = {'title': 'Import'}
    return render(request, 'import.html', {'context': context, })


def upload_file(request):
    """ API для загрузки файлов """
    print(type(request.FILES['file']))
    path = file_save(request.FILES['file'])
    file_read(path)
    return JsonResponse({'status': 'okay'})
