# Напишите функцию, которая принимает на вход строку — 
# абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from os import path as pt



def path(filepath):
    path, filename = pt.split(filepath)
    name, extension = pt.splitext(filename)
    return (f'{path=}\n{name=}\n{extension=}')

st = "F:\Red Dead Redemption 2\Launcher.exe"
print(path(st))

