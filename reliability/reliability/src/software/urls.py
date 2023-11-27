from django.urls import path

from . import views

urlpatterns = [
    path('info', views.info, name='software'),
    path('lipov', views.lipov, name='lipov'),
    path('mills', views.mills, name='mills'),
    path('mills/api/add', views.add_mills),
    path('mills/api/del', views.del_mills),
    path('lipov/api/add', views.add_lipov),
    path('lipov/api/del', views.del_lipov),
    # path('file', views.file),
    # path('api/del', views.delete),
    # path('api/get_plan', views.plan),
    # path('api/save_schem', views.save_schem),
    # path('api/load_schem', views.load_schem),
]
