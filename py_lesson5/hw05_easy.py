#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, shutil


def make_dir(name_dir):
    '''Функция создания директории'''
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Directory {} created successfully'.format(name_dir))
    except OSError:
        print('Directory already exists:', cur_path)


def make_dir_nrm():
    '''Функция для создания директории'''
    name_dir = input('Введите название новой папки:\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Directory {} created successfully'.format(name_dir))
    except OSError:
        print('Directory already exists:', cur_path)


def dir_list():
    '''Функция вывода списка файлов текущей директории'''
    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    print(list_dir)


#     return list_dir

def simple_dir_list():
    '''Функция вывода списка каталогов текущей директории'''
    cur_path = os.getcwd()
    for ddir in os.listdir(cur_path):
        if os.path.isdir(ddir) == True:
            print(ddir)


def del_dir():
    '''Функция удаления директории'''
    name_dir = input('Please enter folder name to delete:\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Directory {} deleted '.format(name_dir))
    except OSError:
        print('Path not found.')


def copy_file():
    '''Функция копирования текущего файла'''
    file_name = sys.argv[0]
    file_name = file_name.split('.py').pop(0) + '_copy.py'
    cur_file = os.path.join(os.getcwd(), sys.argv[0])
    new_file = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(cur_file, new_file)
        print('File write:', new_file)
    except:
        print('Error!')


def change_dir():
    '''Функция смены директории'''
    target = input('Введите название папки или символ "~"\n' \
                   'если хотите перейти в родительский каталог:\n ')
    if target == '~':
        # to_dir = (os.getcwd().split('\\') if os.name == 'nt' else os.getcwd().split('/'))
        # to_dir.pop()
        # to_dir = ('\\'.join(to_dir) if os.name == 'nt' else
        #           '/'.join(to_dir))
        to_dir = os.getenv("HOME")
    else:
        to_dir = os.path.join(os.getcwd(), target)
    try:
        os.chdir(to_dir)
        print('Переход выполнен успешно:', to_dir)
    except OSError:
        print('Переход не возможен!')


if __name__ == '__main__':
    print('Задача-1:')
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    dirlist = ['dir_' + str(n) for n in range(1, 10)]

    for cur_dir in dirlist:
        make_dir(cur_dir)

    print('\nЗадача-2:')
    # Напишите скрипт, отображающий папки текущей директории.
    print(simple_dir_list())

    print('\nЗадача-3:')
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    copy_file()
