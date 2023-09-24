from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='handler'),
    path('api/del', views.delete),
    path('api/upd', views.update),
]
