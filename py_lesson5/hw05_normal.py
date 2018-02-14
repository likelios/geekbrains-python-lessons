#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
import hw05_easy as dirwork


def menu():
    print('Выберете действие (1-4):\n'
          '1. Перейти в папку\n'
          '2. Просмотреть содержимое текущей папки\n'
          '3. Удалить папку\n'
          '4. Создать папку\n'
          'Для выхода введите "q"\n'
          '>>>')
    action = input()
    return action


def handler(action):
    if action == 'q':
        print('Выход из программы...\n''Успешно')
        return
    action_item = {
        '1': dirwork.change_dir,
        '2': dirwork.dir_list,
        '3': dirwork.del_dir,
        '4': dirwork.make_dir_nrm
    }
    item = None
    try:
        item = int(action)
        if item in range(1, 5):
            for item, key in action_item.items():
                if item == action:
                    key()
        else:
            print('"{}" - некорректная команда!'.format(action))

    except ValueError:
        print('"{}" - некорректная команда!'.format(action))

    answer = input('Продолжить работу с программой? -- "y/n"(Да/Нет): ')

    handler(menu()) if answer == 'y' else handler('q')


handler(menu())

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
