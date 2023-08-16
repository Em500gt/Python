#  Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

import os

def rename(wanted_name, count_nums, extension_old, extension_new, diapazon):

    current_dir = os.getcwd()
    files = os.listdir(current_dir)

    for file in files:
        if file.endswith(extension_old):
            file_name = os.path.splitext(file)[0]
            save_diapazon = file_name[diapazon[0] - 1:diapazon[1]]
            count = str(files.index(file) + 1).zfill(count_nums)
            new_file_name = save_diapazon + wanted_name + count + extension_new
            new_file_path = os.path.join(current_dir, new_file_name)
            
            os.rename(file, new_file_path)

rename(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])