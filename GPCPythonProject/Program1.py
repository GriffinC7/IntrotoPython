#Griffin Collins
#program1
Number_of_Weeks = 4
Max_Hours = 160
#Input
employee = input('Employee Name: ')
rate = float(input('Hourly Rate:'))
week1 = float(input('Enter hours worked for week 1: '))
week2 = float(input('Enter hours worked for week 2: '))
week3 = float(input('Enter hours worked for week 3: '))
week4 = float(input('Enter hours worked for week 4: '))

#Processing
totalHours =float(week1+week2+week3+week4)
averageHours =float(totalHours/Number_of_Weeks)
overtimeRate = round(0.05*(rate)+(rate),2)
if totalHours > 160:
    overtimeHours = (totalHours) - 160
    regularHours = totalHours - overtimeHours
    print(\nemployee, 'worked',overtimeHours, 'hours of overtime.')
 
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
