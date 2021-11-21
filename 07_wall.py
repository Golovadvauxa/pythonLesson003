# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x1, y1 = 0, 0
x2, y2 = 100, 50
point1 = sd.get_point(x1, y1)
point2 = sd.get_point(x2, y2)
for i in range(0, 601, 50):
    y1 = i
    y2 = i + 50
    for j in range(0, 1201, 50):
        if i % 20 != 0 and j % 20 == 0:
            x1 = j
            x2 = j + 100
            point1 = sd.get_point(x1, y1)
            point2 = sd.get_point(x2, y2)
            sd.rectangle(point1, point2, width=3)
        elif i % 20 == 0 and j % 20 != 0:
            x1 = j
            x2 = j + 100
            point1 = sd.get_point(x1, y1)
            point2 = sd.get_point(x2, y2)
            sd.rectangle(point1, point2, width=3)

sd.pause()
