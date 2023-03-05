# -------------------------------------------------------------
# Author: Griffin Collins
# Program: Program3
#
# Description:
# This program provides an invoice statement like program1 
# It can also add another employee and can validate the employee name, rate, and numeber of hours worked each weeks
# -------------------------------------------------------------
def main ():
    import BillingModule
    NUMBER_OF_WEEKS = 4
    MAX_HOURS = 160
    RATE_INCREASE = 0.05
    again = 'Y'
    #Input
    while again == 'Y' or again == 'y':
        prompt ='\nEmployee Name:'
        employee = BillingModule.readEmployeeName(prompt)
        ratePrompt = 'Hourly Rate:'
        rate = BillingModule.readHourlyRate(ratePrompt)
        weekPrompt = 'Enter hours worked for week 1: ' 
        week1 = BillingModule.readWeeklyHours(weekPrompt)
        weekPrompt = 'Enter hours worked for week 2: '
        week2 = BillingModule.readWeeklyHours(weekPrompt)
        weekPrompt = 'Enter hours worked for week 3: '
        week3 = BillingModule.readWeeklyHours(weekPrompt)
        weekPrompt = 'Enter hours worked for week 4: '
        week4 = BillingModule.readWeeklyHours(weekPrompt)
        
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
            otDueString ='Overtime hours: '+format(overtimeHours, ',.2f')+' @ $'+\
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

main()
