# coding: utf8
# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

print ('<<Задача1-normal>>')

chislododesyati = int(input('Введите число:'))

while chislododesyati <= 0 or chislododesyati >= 10:
    chislododesyati = int(input('Введите число заново - больше 0  - но меньше 10:'))
print ('Число возведенное в степень 2:', chislododesyati**2)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:

# * постарайтесь сделать решение через действия над числами;
print('<<Задача2-normal>>')

znacha = int(input('Введите первое заначение:'))
znachb = int(input('Введите второе заначение:'))

print('Вы ввели:', znacha, znachb)

znacha ^= znachb
znachb ^= znacha
znacha ^= znachb

print('Махнем местами:', znacha, znachb)







