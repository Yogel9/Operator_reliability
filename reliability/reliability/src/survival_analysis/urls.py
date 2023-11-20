from django.urls import path

from . import views

urlpatterns = [

    path('info', views.info, name='survival'),
    path('graph', views.graph, name='graph'),
    path('api/del', views.delete),
    path('api/save_schem', views.save_schem),
    path('api/load_schem', views.load_schem),
]
