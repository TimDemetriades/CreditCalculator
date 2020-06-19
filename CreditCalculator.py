def count_of_months(monthly_payment, principal):
    if (principal / monthly_payment).is_integer():
        return int(principal / monthly_payment)
    else:
        return int(principal // monthly_payment + 1)
def monthly_payment(months, principal):
    if (principal / months).is_integer():
        return int(principal / months)
    else:
        payment = int(principal // months + 1)
        return (payment, principal - (months - 1) * payment)    # return list/tuple

while True:
    try:
        principal = int(input('Enter the credit principal: '))
    except ValueError:
        print('Please enter a number')
    else:
        print(principal)
        break
while True:
    option = input('What do you want to calculate?\nType "m" - for count of months,\nType "p" - for monthly payment\n')
    if option == 'm':
        monthly_payment = int(input('Enter monthly payment: '))
        months = count_of_months(monthly_payment, principal)
        if months != 1:
            print(f'\nIt takes {months} months to repay the credit\n')
        else:
            print(f'\nIt takes 1 month to repay the credit\n')
        break
    elif option == 'p':
        months = int(input('Enter count of months: '))
        monthly_payment = monthly_payment(months, principal)
        if isinstance(monthly_payment, int):        # check if integer or list/tuple was returned
            print(f'\nYour monthly payment = {monthly_payment}\n')
        else:
            print(f'\nYour monthly payment = {monthly_payment[0]} with last month payment = {monthly_payment[1]}\n')
        break
    else:
        print('Please enter either "m" or "p"')