# Все задачи текущего блока решите с помощью генераторов списков!

print('Задание-1:\n')
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

listparam = dict(listlen=int(input('Введите длину списка: ')), minlist=int(input('Минимальное: ')),
                 maxlist=int(input('Максимальное: ')))
i = 0
randolist = []
while i < listparam['listlen']:
    randoint = random.randint(listparam['minlist'], listparam['maxlist'])
    randolist.append(randoint)
    i += 1

print('Исходный список: ', randolist)

randolistxx2 = []
for i in randolist[:]:
    randointxx2 = i ** 2
    randolistxx2.append(randointxx2)

print('Искомый список: ', randolistxx2)

print('\nЗадание-2:\n')
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruitone = ['Яблоко', 'Манго', 'Персик', 'Ананас']
fruittwo = ['Груша', 'Вишня', 'Персик', 'Айва', 'Ананас', 'Айва']
fruituniclist = set(fruitone) & set(fruittwo)

print(fruituniclist)

print('\nЗадание-3:\n')
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
# Можем взять список из Задание-1 ?
print('Лист из первой задачи(случайный):', randolist)


def newlist3not4(inputlist):
    clearlist = []
    for item in inputlist:
        if item % 3 == 0 and item % 4 != 0 and item > 0:
            clearlist.append(item)
    return clearlist

print('Наш список:',list(newlist3not4(randolist)))

