# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }

import os
import json
import csv
import pickle

path = 'D:/Python/Homework/Homework8'

def get_directory_info(directory):
    directory_info = []
    
    for dirs, _, files in os.walk(directory):
        folder_size = sum(os.path.getsize(os.path.join(dirs, file)) for file in files)
        
        directory_info.append(
            {
                'Name': os.path.basename(dirs),
                'Parents': dirs.split(r'/')[-2],
                'Type': 'Directory',
                'Size': folder_size
            }
        )
        
        for file in files:
            file_path = os.path.join(dirs, file)
            file_size = os.path.getsize(file_path)
            
            directory_info.append(
                {
                    'Name': file,
                    'Parents': dirs.split(r'/')[-1],
                    'Type': 'File',
                    'Size': file_size
                }
            )
    
    return directory_info

def save_directory_info(directory):
    directory_info = get_directory_info(directory)
    
    with open('directory_info.json', 'w') as json_file:
        json.dump(directory_info, json_file, indent=3)
    
    with open('directory_info.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Type', 'Size'])
        write_directory_info_to_csv(directory_info, writer)

    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(directory_info, pickle_file)

def write_directory_info_to_csv(directory_info, writer):
    for item in directory_info:
        writer.writerow([item['Name'], item['Type'], item['Size']])
        
        if item['Type'] == 'Directory':
            writer.writerow(['-'] * 3)

save_directory_info(path)