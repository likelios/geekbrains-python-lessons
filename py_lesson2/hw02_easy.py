print('Задача-1:')
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()


fruitlist = ['яблоко', 'банан', 'киви', 'арбуз', 'ананас']
fruitlen = int(len(fruitlist))
i = 0
while i < fruitlen:
    print(str(i+1)+'.', end=' ')
    print((fruitlist[i]).rjust(6, ' '))
    i += 1


print('Задача-2:')
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
fruitlista = ['яблоко', 'банан', 'киви', 'арбуз', 'ананас']
fruitlistb = ['киви', 'арбуз', 'ананас']
result=list(set(fruitlista) - set(fruitlistb))
print(result)



print('Задача-3:')
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
listinta = [-8,1,6,3,8,1,9,12,112,8,144]
listintb = []
lenlist = len(listinta)
print('Длина списка: ',lenlist)
i = 0
while  i < lenlist:
    if listinta[i] % 2 == 0:
        listintb.append(listinta[i] / 4)
        # print('Кратно двум: ', listinta[i])
    elif listinta[i] % 2 != 0:
        listintb.append(listinta[i] * 2)
        # print('Не Кратно двум: ', listinta[i])
    i += 1
print('Исходный: ',listinta)
print('Искомый: ',listintb)

