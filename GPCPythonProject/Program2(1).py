#Griffin Collins
#program2
Number_of_Weeks = 4
Max_Hours = 160
minimumRate = 20.0
minimumHours = 35
maximumHours = 80
again = 'Y'
#Input
while again == 'Y' or again == 'y':
    employee = input('Employee Name: ')
    while len(str(employee)) <= 1:
        print('Employee name must be entered.')
        employee = input('\nEmployee Name: ')
    rate = float(input('Hourly Rate:'))
    while rate < 20.00:
        print("Rate must be at least $20.00/hour.")
        rate = float(input('\nHourly Rate:'))
    week1 = float(input('Enter hours worked for week 1: '))
    while week1 > 80 or week1 < 35:
        print('Number of hours worked must be between 35 and 80.')
        week1 = float(input('\nEnter hours worked for week 1: '))
    week2 = float(input('Enter hours worked for week 2: '))
    while week2 > 80 or week2 < 35:
        print('Number of hours worked must be between 35 and 80.')
        week2 = float(input('\nEnter hours worked for week 2: '))
    week3 = float(input('Enter hours worked for week 3: '))
    while week3 > 80 or week3 < 35:
        print('Number of hours worked must be between 35 and 80.')
        week3 = float(input('\nEnter hours worked for week 3: '))
    week4 = float(input('Enter hours worked for week 4: '))
    while week4 > 80 or week4 < 35:
        print('Number of hours worked must be between 35 and 80.')
        week4 = float(input('\nEnter hours worked for week 4: '))
     

    #Processing
    totalHours =float(week1+week2+week3+week4)
    averageHours =float(totalHours/Number_of_Weeks)
    overtimeRate = round(0.05*(rate)+(rate),2)
    if totalHours > 160:
        overtimeHours = (totalHours) - 160
        regularHours = totalHours - overtimeHours
        print()
        print(employee, 'worked',overtimeHours, 'hours of overtime.')
     
    else:
        overtimeHours = 0
        overtimeAmount = 0
        regularHours = totalHours
        print()
        print(employee, "worked no overtime.")
    regularAmount = regularHours * rate
    overtimeAmount = overtimeRate * overtimeHours
    invoiceAmount = float(regularAmount + overtimeAmount)    

    #Output
    print('\nInvoice')
    print('Resource: ',employee,'\tAverage weekly hours: ',format(averageHours, '.2f'))
    print('\nTotal billable hours: ',\
     format(totalHours, '.2f'),'\trate: $',\
     format(rate, '.2f'), sep='')
    print('Overtime hours: ',format(overtimeHours, '.2f'),' @ $', overtimeRate , '\t= $',\
          format(overtimeAmount, ',.2f'),sep='')
    print('Regular hours: ',format(regularHours, '.2f'),' @ $', format(rate, ',.2f') , '\t= $',\
          format(regularAmount, ',.2f'),sep='')
    print('Amount Due: $',format(invoiceAmount, ',.2f'), sep='')

    again = input('\nAdd another Employee? ("y"=yes): ')
