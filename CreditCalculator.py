# Credit Calculator
# By: Tim Demetriades
# Date: 6/19/2020

import math

def month_to_year_converter(months):
    years = int(months / 12)
    months = months % 12
    return (years, months)

def number_checker(string):
    while True:
        try:
            string
        except ValueError:
            print('Please enter a number')
        else:
            break

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

while True:
    option = input('What do you want to calculate?\ntype "n" - for count of months,\ntype "a" - for annunity monthly payment\ntype "p" - for credit principal:\n')
    if option == 'n':       # Calculate count of years/months to pay off credit
        principal = float(input('Enter credit principal:\n'))
        monthly_payment = float(input('Enter monthly payment:\n'))
        interest = float(input('Enter credit interest:\n'))
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
        principal = float(input('Enter credit principal:\n'))
        months = float(input('Enter count of periods:\n'))
        interest = float(input('Enter credit interest:\n'))

        monthly_payment = math.ceil(monthly_payment(principal, months, interest))
        print(f'Your annuity payment = {monthly_payment}!')
        break
    elif option == 'p':     # Calculate credit principal
        number_checker(monthly_payment = float(input('Enter monthly payment:\n')))
        months = float(input('Enter count of periods:\n'))
        interest = float(input('Enter credit interest:\n'))

        principal = math.floor(principal(monthly_payment, months, interest))
        print(f'Your credit principal = {principal}!')
        break
    else:
        print('Please enter either "m" or "p"')
