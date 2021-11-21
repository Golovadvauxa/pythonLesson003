# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    point = sd.get_point(x, y)
    sd.circle(point, 50, color)
    point = sd.get_point(x - 20, y + 10)
    sd.circle(point, 5, color)
    point = sd.get_point(x + 20, y + 10)
    sd.circle(point, 5, color)
    point1 = sd.get_point(x - 25, y - 25)
    point2 = sd.get_point(x + 25, y - 20)
    sd.ellipse(point1, point2, color)
    point1 = sd.get_point(x - 10, y - 30)
    point2 = sd.get_point(x + 10, y - 30)
    sd.square(point1, 5, color)
    sd.square(point2, 5, color)


for _ in range(10):
    x = random.randint(50, 1150)
    y = random.randint(50, 550)
    color = sd.random_color()
    smile(x, y, color)
sd.pause()
