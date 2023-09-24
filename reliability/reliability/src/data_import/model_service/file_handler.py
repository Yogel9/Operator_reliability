import os

from django.core.files.storage import FileSystemStorage


def file_save(file) -> str:
    """ Сохраняем файл """
    file_dir = os.getcwd() + "\\files"
    fs = FileSystemStorage(location=file_dir)
    path = fs.save(file.name, file)
    return file_dir + path


def file_read(path: str) -> str:
    """ Заносим считанные данные в базу """
    path = ''
    return path
