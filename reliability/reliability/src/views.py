from django.shortcuts import render


def main_index(request):
    """ Главная страница с разъяснительной информацией """
    context = {"title": 'Главная'}
    return render(request, 'base.html', {'context': context, })

