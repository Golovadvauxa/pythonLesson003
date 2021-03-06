# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# x1, y1 = 50, 50
# x2, y2 = 350, 450
# for color in rainbow_colors:
#     start_point = sd.get_point(x1, y1)
#     end_point = sd.get_point(x2, y2)
#     sd.line(start_point, end_point, color, 4)
#     x1 += 5
#     x2 += 5

    # Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 500
point = sd.get_point(500, -100)
for color in rainbow_colors:
    sd.circle(point, radius, color, 10)
    radius-=10

sd.pause()
