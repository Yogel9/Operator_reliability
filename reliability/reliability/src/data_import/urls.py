from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='import_file'),
    path('api/upload_file', views.upload_file),

]
