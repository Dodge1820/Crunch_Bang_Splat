#Mortgage_calculator
#Shay Dodge
#01/27/2020
#CS1181-05
#Jon Holmes
#This is a mortgage calculator used to determine one's total monthly payment based on their home loan amount,their annual interest rate,and their loan duration.

total_amount_string = input("What is the total amount of your home loan? $")
rate_string = input("What is the annual interest rate of the loan? %")
duration_in_months_string = input("How long is the length of your loan in months?")
total_amount_float = (float(total_amount_string))
rate_float = (float(rate_string))
duration_in_months_float = (float(duration_in_months_string))


monthly_rate = ((int(rate_float) /100) / 12)
#print("Your monthly interest rate is", monthly_rate)


total_monthly_payment_numerator = monthly_rate * ((1 + monthly_rate) ** duration_in_months_float)
#print(total_monthly_payment_numerator)

total_monthly_payment_denominator = ((1 + monthly_rate)** duration_in_months_float) - 1
#print(total_monthly_payment_denominator)

total_monthly_payment = total_amount_float * (total_monthly_payment_numerator / total_monthly_payment_denominator)
print("Your total monthly mortgage payment would be $", total_monthly_payment)







