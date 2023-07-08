##############################################################
#              calculate the cans of paint required          #
##############################################################

import math

#calculate the required cans of paint
def paint_calc(height, width, cover):
    paint = (height * width) / cover

    print(f"you'll need {math.ceil(paint)} cans of paint")

#get mesaurements of height and width of a wall
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)