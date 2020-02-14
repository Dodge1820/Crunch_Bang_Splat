# Shay Dodge
# 2/4/20
# CS 1181-05

#ask for user input for sides, length, and angles
lines = input("How many lines would you like to draw?")
line_length= input("What equal length would you like to set for all of your lines?")
what_degree = input("At what degree would you like your turns?")


#import turtle code and create screen and turle
import turtle
walgreens_pharmacy = turtle.Screen()
walgreens_pharmacy.bgcolor("gray")
slave_to_society = turtle.Turtle()
slave_to_society.pensize(16)
slave_to_society.speed(25)
slave_to_society.color("aquamarine")




for i_need_my_norcos in range(int(lines)):
    slave_to_society.forward(int(line_length))
    slave_to_society.left(int(what_degree))

walgreens_pharmacy.exitonclick()
