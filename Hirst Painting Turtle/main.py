# import colorgram
#
# number_of_color = int(input("How many colors do you want to get as RGB Tuple? (>0): "))
# colors = colorgram.extract("image.jpg", number_of_color+1)
# color_as_RGB = []
#
# for _ in range(0, number_of_color):
#     color = colors[_]
#     color_rgb = color.rgb
#     get_it = (color_rgb[0], color_rgb[1], color_rgb[2])
#     color_as_RGB.append(get_it)
import turtle as t
from random import *

colors_got = [
    (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
    (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
    (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
    (159, 177, 54), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
    (151, 206, 220)
]

bug = t.Turtle()
t.colormode(255)


def line_dots(turtle_name):
    turtle_name.penup()
    turtle_name.goto(-200, -200)
    turtle_name.speed(0)
    row = 0
    set = -200
    end = False
    while not end:
        for _ in range(10):
            turtle_name.dot(20, choice(colors_got))
            turtle_name.fd(50)
        row += 1
        if row <= 9:
            set += 50
            turtle_name.goto(-200, set)
        elif row == 10:
            turtle_name.goto(-200, -200)
            end = True
        else:
            turtle_name.goto(-200, -200)
            end = False


line_dots(bug)


screen = t.Screen()
screen.exitonclick()
screen.title("I am doing this shit!")
