from django.shortcuts import render

# Create your views here.


def index(request):
    """Страница для работы с таблицей данных"""
    context = {'title': 'Handler'}
    return render(request, 'table.html', {'context': context, })

