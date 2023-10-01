import colorgram

# rgb_color = []
# colors = colorgram.extract('img.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_rgb = (r, g, b)
#     rgb_color.append(tuple_rgb)
# print(rgb_color)
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


tim.penup()     # remove lines
tim.hideturtle()    # hide turtle

# setting the starting point of tim for painting, SETHEADING means giving direction
tim.setheading(225)  # 225 = (180+270)/2 degrees
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

num_of_dots = 101
for dot_count in range(1, num_of_dots):
    tim.dot(20, random.choice(color_list))  # (size,'color')
    tim.forward(50)  # (distance)

    if dot_count % 10 == 0:
        tim.setheading(90)  # turn turtle by 90 degrees
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()  # making an object for displaying screen
screen.exitonclick()  # add clickonexit option to screen
