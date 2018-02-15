#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('Задача - 1\n')


# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, model, color, speed, is_police=False):
        self.model = model
        self.color = color
        self.speed = speed
        self.police = is_police

    def go(self):
        return "поехал"

    def stop(self):
        return "остановился"

    def turn(self, direction):
        return "повернул {}".format(direction)


class SportCar:

    def __init__(self, model, color, speed, is_police=False):
        self.model = towncar_model
        self.color = towncar_color
        self.speed = towncar_speed
        self.police = is_police

    def go(self):
        return "поехал"

    def stop(self):
        return "остановился"

    def turn(self, direction):
        return "повернул {}".format(direction)


car1 = TownCar('Черный авто', "черный", "60 км/час", False)
print(car1.model, car1.color, car1.go(), car1.speed, car1.turn("направо"), \
      car1.stop(), car1.police)

print('Задача - 2\n')


# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
# ==================================================================


# Родительский:
class Car:
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        self.type = car_type
        self.model = car_model
        self.color = car_color
        self.speed = car_speed
        self.police = is_police

    def go(self):
        return "поехал"

    def stop(self):
        return "остановился"

    def turn(self, direction):
        return "повернул {}".format(direction)


# Производный класс:
class Towncar1(Car):
    def __init__(self, car_type, car_model, car_color, car_speed, is_police=False):
        super().__init__(car_type, car_model, car_color, car_speed, is_police=False)


town_car = Towncar1("Городской ", "автомобиль Lada Granta", "черный", \
                    "60 км/час", is_police=False)
print(town_car.type, town_car.model, town_car.color, town_car.go(), town_car.speed, \
      town_car.turn("налево"), town_car.stop(), car1.police)
