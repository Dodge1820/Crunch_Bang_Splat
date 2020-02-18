#Shay Dodge
#2/17/20
#CS 1181-05
#Prof. Jon Holmes


#import roman numerals
import roman_numerals

#ask user to enter number
first_number = int(input("Enter a number between 1 and 5:"))
#decide if number entered falls B/W 1 and 5
if roman_numerals.check_extents (1, 5, first_number):
    #ask for second_number from user
    second_number = int(input("Enter a second number between 1 and 5:"))
    #decide if second number entered falls B/W 1 and 5
    if roman_numerals.check_extents(1, 5, second_number):
        #If both numbers were valid then sum the two numbers up
        sum_of_user_numbers = first_number + second_number
        #Print the roman numeral representation of the sum
        roman_numeral_representation = roman_numerals.get_roman_numeral(sum_of_user_numbers)
        print(roman_numeral_representation)
    #Otherwise, let user know if number entered is invalid
    else:
        print("Second number is invalid.")
#Otherwise, let user know if number entered is invalid
else:
    print("First number is invalid.")




























