from django.urls import path

from . import views

urlpatterns = [

    path('info', views.info, name='operator'),
    path('', views.index, name='handler'),
    path('file', views.file, name='import_file'),
    path('api/del', views.delete),
    path('api/upd', views.update),
    path('api/add', views.add),
    path('api/upload_file', views.upload_file),
]
