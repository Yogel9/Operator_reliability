from django.urls import path

from . import views

urlpatterns = [

    path('info', views.info, name='devices'),
    path('scheme', views.scheme, name='scheme'),
    path('file', views.file),
    path('api/del', views.delete),
    path('api/get_plan', views.plan),
    path('api/save_schem', views.save_schem),
    path('api/load_schem', views.load_schem),
]
