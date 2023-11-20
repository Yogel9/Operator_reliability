from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from survival_analysis.models import Equipment
from survival_analysis.model_service.file import SchemSaver, SchemLoader
from survival_analysis.model_service.survive import get_graph_data


def info(request):
    """ Информация по модулю """
    context = {'pre_title': 'Info',
               'title': 'Survival', }
    return render(request, 'survival_index.html', {'context': context, })


def graph(request):
    """ Страница с таблицей и графиком """
    context = {'pre_title': 'Graph',
               'title': 'Survival',
               'equipments': Equipment.objects.all(),
               'graph_data': get_graph_data(),
               'param': {'Max': 0, 'St': 0, 'Min': 0}}

    if request.method == "POST":
        if 'operating_time' in request.POST:
            index = 0
            find_time = float(request.POST['operating_time'])
            for time in context['graph_data']['t']:
                if find_time > time:
                    index = context['graph_data']['t'].index(time)
                else:
                    break
            context['param']['T'] = find_time
            context['param']['Max'] = context['graph_data']['dsMax'][index]
            context['param']['St'] = context['graph_data']['st'][index]
            context['param']['Min'] = context['graph_data']['dsMin'][index]

        if 'time' in request.POST:
            try:
                Equipment.objects.create(time=request.POST['time'],
                                         surviving_obj=request.POST['surviving_obj'],
                                         failed_obj=request.POST['failed_obj'],
                                         probability=request.POST['probability'])
            except ValueError:
                print('Не все поля корректно заполнены!')

    print(context['graph_data'])
    return render(request, 'graph.html', {'context': context, })


def delete(request):
    """ API-Удаление элемента по id"""
    Equipment.objects.get(id=request.POST['id']).delete()
    return JsonResponse({"status": f'Элемент ID:{request.POST["id"]} удалён'})


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
