#Shay Dodge
#02/07/20
#CS 1181-05
#Prof. Jon Holmes
#This is a program designed to provide customers with a quote on their carpet order (based off of their desired sq.ft. and cost of carpet)


#define 3 functions

def convert_inches_to_feet(inches):
    """converts length and width from inches to feet
    :param inches
    :return inches converted to ft."""

    feet = inches / 12
    return feet



def calculate_square_footage (length, width):
    """calc. square footage
    :param length of room, width of room
    :return total sq. ft. of room"""

    total_sq_ft = length * width
    return total_sq_ft



def calculate_room_price (length, width, carpet_cost_per_sq_ft):
    """calculates total cost of carpet for room
    :param length, width, carpet cost per sq ft
    :return total cost of carpet for room"""

    inches_to_ft_for_length = convert_inches_to_feet(length)
    inches_to_ft_for_width = convert_inches_to_feet(width)
    total_sq_ft = calculate_square_footage(inches_to_ft_for_length, inches_to_ft_for_width)

    return total_sq_ft * carpet_cost_per_sq_ft






#get input for number of rooms (number of times to run loop)
how_many_rooms = int(input("How many rooms would you like to carpet?"))

#setting up increment for total the cost of the carpet order
total_carpet_order = 0

#setting up increment for room number
room_number = 1



#create loop to collect input and call functions to calculate total cost of carpet order
for carpet_cost in range (how_many_rooms):
    length_in_inches = float(input("What is the length of room {} in inches?".format(room_number)))
    width_inches = float(input("What is the width of room {} in inches?".format(room_number)))
    price_per_sq_ft = float(input("What is the price of the carpet per square foot?"))

    total_cost_of_room = round(float(calculate_room_price (length_in_inches, width_inches, price_per_sq_ft)), 2)
    print ("This room will cost $",total_cost_of_room, "to carpet.")
    total_carpet_order += total_cost_of_room
    room_number += 1

print("The total price for your carpet order will be $", total_carpet_order,".")


































