import colorgram
import turtle as turtle_module
import random

color_list = [(239, 229, 213), (203, 161, 18), (217, 155, 70), (242, 230, 236), (49, 104, 158), (207, 151, 182), (226, 207, 135), (187, 66, 39), (229, 234, 242), (162, 29, 36), (29, 28, 69), (232, 240, 234), (36, 79, 40), (28, 67, 32), (143, 161, 183), (168, 43, 50), (76, 104, 77), (151, 30, 27), (150, 169, 152), (193, 93, 76), (219, 172, 193), (229, 174, 165), (181, 96, 102), (105, 125, 159), (51, 51, 88), (180, 189, 210), (65, 34, 20), (113, 138, 114), (181, 199, 183), (67, 24, 39)]

# # Extract colors from an image
# colors = colorgram.extract('hirst.painting.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
t = turtle_module.Turtle()
t.speed('fastest')
t.penup()
change_y = -50
y = -250
for _ in range(10):
    y = y - change_y
    t.goto(-250, y)
    for _ in range(10):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)

t.hideturtle()
screen = turtle_module.Screen()
screen.exitonclick()
