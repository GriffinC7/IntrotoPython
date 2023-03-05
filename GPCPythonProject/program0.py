#Griffin Collins
#program0
Number_of_Weeks = 4
totalHours = 0.0
averageHours = 0.0
employee = input('Employee Name: ')
rate = float(input('Hourly Rate:'))
week1 = float(input('Enter hours worked for week 1: '))
week2 = float(input('Enter hours worked for week 2: '))
week3 = float(input('Enter hours worked for week 3: '))
week4 = float(input('Enter hours worked for week 4: '))

#Processing
totalHours =float(week1+week2+week3+week4)

averageHours =float(totalHours/Number_of_Weeks)

invoiceAmount = float(rate*totalHours)


print('\nInvoice')
print('Resource: ',employee,'\tAverage weekly hours: ',format(averageHours, '.2f'))
print('\nTotal billable hours: ',\
 format(totalHours, '.2f'),'\trate: $',\
 format(rate, '.2f'), sep='')
print('Amount Due: $',format(invoiceAmount, ',.2f'), sep='')
