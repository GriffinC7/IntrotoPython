# -------------------------------------------------------------
# Author: Griffin Collins
# Program: Program2
#
# Description:
# This program provides an invoice statement like program1 
# It can also add another employee and can validate the employee name, rate, and numeber of hours worked each weeks
# -------------------------------------------------------------
NUMBER_OF_WEEKS = 4
MAX_HOURS = 160
MIN_RATE = 20.0
MIN_HOURS = 35
MAX_HOURS_PER_WEEK = 80
RATE_INCREASE = 0.05
again = 'Y'
#Input
while again == 'Y' or again == 'y':
    employee = input('Employee Name: ')
    while len(employee) < 1:
        print('\nError: Employee name must be entered.')
        employee = input('\nEmployee Name: ')
    rate = float(input('Hourly Rate:')) 
    while rate <= MIN_RATE:
        print("\nError: Rate must be greater than $20.00/hour.")
        rate = float(input('\nHourly Rate:'))
    week1 = float(input('Enter hours worked for week 1: ')) 
    while week1 > MAX_HOURS_PER_WEEK or week1 < MIN_HOURS:
        print('\nError: Number of hours worked must be between 35 and 80.')
        week1 = float(input('\nEnter hours worked for week 1: '))  
    week2 = float(input('Enter hours worked for week 2: '))
    while week2 > MAX_HOURS_PER_WEEK or week2 < MIN_HOURS:
        print('\nError: Number of hours worked must be between 35 and 80.')
        week2 = float(input('\nEnter hours worked for week 2: '))
    week3 = float(input('Enter hours worked for week 3: '))
    while week3 > MAX_HOURS_PER_WEEK or week3 < MIN_HOURS:
        print('\nError: Number of hours worked must be between 35 and 80.')
        week3 = float(input('\nEnter hours worked for week 3: '))
    week4 = float(input('Enter hours worked for week 4: '))
    while week4 > MAX_HOURS_PER_WEEK or week4 < MIN_HOURS:
        print('\nError: Number of hours worked must be between 35 and 80.')
        week4 = float(input('\nEnter hours worked for week 4: '))
    #Processing       
    totalHours = float(week1+week2+week3+week4)
    averageHours = float(totalHours/NUMBER_OF_WEEKS)
    if totalHours > MAX_HOURS:
        overtimeHours = totalHours - MAX_HOURS
        overtimeRate = rate + round(RATE_INCREASE * rate,2)
        overtimeAmount = round(overtimeRate * overtimeHours,2)
        regularHours = totalHours - overtimeHours
        regularAmount = regularHours * rate
        overtimeString = '\n'+employee+' worked '+str(overtimeHours)+' hours of Overtime.'
        otDueString =        'Overtime hours: '+format(overtimeHours, ',.2f')+' @ $'+\
                format(overtimeRate, ',.2f')+' \t= $'+\
                format(overtimeAmount, ',.2f')+'\n'
        
    else:
        overtimeHours = ""
        overtimeAmount = 0.0
        regularHours = totalHours
        regularAmount = totalHours * rate
        overtimeString = '\n'+employee+' worked no overtime.'
        otDueString = ''
    invoiceAmount = float(regularAmount + overtimeAmount)    

    #Output
    print(overtimeString)
    print('\nInvoice')
    print('Resource: ',employee,'\tAverage weekly hours: ',\
          format(averageHours, '.2f'))
    print('\nTotal billable hours: ',\
     format(totalHours, '.2f'),'\trate: $',\
     format(rate, '.2f'), sep='')


    
    print(otDueString, end='')
    print('Regular hours: ',format(regularHours, '.2f'),' @ $',\
          format(rate, ',.2f') , '\t= $',\
          format(regularAmount, ',.2f'),sep='')
    print('Amount Due: $',format(invoiceAmount, ',.2f'), sep='')

    again = input('\nWould you like to add another employee: ')
