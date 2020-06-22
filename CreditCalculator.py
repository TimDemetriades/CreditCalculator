# Credit Calculator
# By: Tim Demetriades
# Date: 6/19/2020

import math

def month_to_year_converter(months):
    # Converts months to years/months
    years = int(months / 12)
    months = months % 12
    return (years, months)

def number_checker(prompt, num_type):
    # Checks if user entered a number
    while True:
        try:
            value = num_type(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue

        if value < 0:
            print("Please enter a positive number.")
            continue
        else:
            break
    return value

def count_of_months(principal, monthly_payment, interest):
    nominal_interest = interest / (12 * 100)     # 12 months, 100%
    x = monthly_payment / (monthly_payment - nominal_interest * principal)
    if math.log(x, 1 + interest).is_integer():
        return math.log(x, 1 + interest)
    else:
        return math.ceil(math.log(x, 1 + nominal_interest))
        
def monthly_payment(principal, months, interest):
    nominal_interest = interest / (12 * 100)     # 12 months, 100%
    return principal * ((nominal_interest * pow(1 + nominal_interest, months)) / (pow(1 + nominal_interest, months) - 1))

def principal(monthly_payment, months, interest):
    nominal_interest = interest / (12 * 100)     # 12 months, 100%
    return monthly_payment / ((nominal_interest * pow(1 + nominal_interest, months)) / (pow(1 + nominal_interest, months) - 1))

# Main loop
while True:
    option = input('What do you want to calculate?\n'
                   'type "n" - for count of months,\n'
                   'type "a" - for annunity monthly payment\n'
                   'type "p" - for credit principal:\n')
                   
    if option == 'n':       # Calculate count of years/months to pay off credit
        principal = number_checker('Enter credit principal:\n', float)
        monthly_payment = number_checker('Enter monthly payment:\n', float)
        interest = number_checker('Enter credit interest:\n', float)
        months = count_of_months(principal, monthly_payment, interest)

        time = month_to_year_converter(months)
        if time[0] == 0:
            if months != 1:
                print(f'\nYou need {months} months to repay this credit!\n')
            else:
                print(f'\nYou need 1 month to repay this credit!\n')
        else:
            print(f'You need {time[0]} years and {time[1]} months to repay this credit!')
        break
    elif option == 'a':     # Calculate monthly/annuinty payment
        principal = number_checker('Enter credit principal:\n', float)
        months = number_checker('Enter count of periods:\n', float)
        interest = number_checker('Enter credit interest:\n', float)

        monthly_payment = math.ceil(monthly_payment(principal, months, interest))
        print(f'Your annuity payment = {monthly_payment}!\n')
        break
    elif option == 'p':     # Calculate credit principal
        monthly_payment = number_checker('Enter monthly payment:\n', float)
        months = number_checker('Enter count of periods:\n', float)
        interest = number_checker('Enter credit interest:\n', float)

        principal = math.floor(principal(monthly_payment, months, interest))
        print(f'Your credit principal = {principal}!\n')
        break
    else:
        print('Please enter either "m" or "p"')
