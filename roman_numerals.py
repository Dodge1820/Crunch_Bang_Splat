#Shay Dodge
#2/17/20
#CS 1181-05
#Prof. Jon Holmes

#create check_extents which takes 3 parameters (integers) and returns a boolean value
def check_extents(min, max, value_to_check):
    '''checks parameters against the user input
    :param min: lowest number that the value can be
    :param max: Highest number that the value can be
    :param value_to_check: number the user inputs
    :return True, if value input is b/w min and max, inclusive'''


    if value_to_check >= min and value_to_check <= max:
        return True
    else:
        return False








#create get_roman_numerals, which takes one integer parameter and returns the roman numeral representation as a string
def get_roman_numeral(sum_of_user_numbers):
    '''takes one integer parameter and returns the roman numeral representation as a string
    :param: sum_of_user_numbers
    :return: roman numeral representation of sum_of_user_numbers'''


    if sum_of_user_numbers == 1:
        return ("I")
    elif sum_of_user_numbers == 2:
        return ("II")
    elif sum_of_user_numbers == 3:
        return("III")
    elif sum_of_user_numbers == 4:
        return("IV")
    elif sum_of_user_numbers == 5:
        return("V")
    elif sum_of_user_numbers == 6:
        return("VI")
    elif sum_of_user_numbers == 7:
        return("VII")
    elif sum_of_user_numbers == 8:
        return("VIII")
    elif sum_of_user_numbers == 9:
        return("IX")
    else:
        # sum_of_user_numbers == 10:
        return("X")







