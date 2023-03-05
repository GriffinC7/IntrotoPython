#-----------------------------
# Module for Program4
# Author: Griffin Collins
#-----------------------------
def readEmployeeName(prompt):
    employee = input(prompt)
    while len(employee) < 1:
        print('\nError: Employee name must be entered.')
        employee = input('\n' + prompt)
    return employee



def readHourlyRate(ratePrompt):
    MIN_RATE = 20.0
    again = True
    while again:
        try:
            rate = float(input(ratePrompt))
            if rate <= MIN_RATE:
                print("\nError: Rate must be greater than $20.00/hour.\n")
            else:
                again = False
        except ValueError:
            print("\nError: Rate must be greater than $20.00/hour.\n")
    return rate


def readWeeklyHours(weekPrompt):
    MIN_HOURS = 35
    MAX_HOURS = 80
    again = True
    while again:
        try:  
            week = float(input(weekPrompt))
            if week > MAX_HOURS or week < MIN_HOURS:
                print('\nError: Number of hours worked must be between 35 and 80.\n')
            else:
                again = False
        except ValueError:
            print('\nError: Number of hours worked must be between 35 and 80.\n')         
    return week
                     
    
def resetBillingFile( file ):
    outfile = open( file , 'w').close()

def writeBillingRecord(employee, rate, week1, week2, week3, week4):
    outfile = open('Billing.txt','a')

    outfile.write(employee + '\n'
                    + str(rate)+ '\n'
                    + str(week1)+ '\n'
                    + str(week2)+ '\n'
                    + str(week3)+ '\n'
                    + str(week4)+ '\n')
                    
    outfile.close()


def readString(file):
    return file.readline().rstrip('\n')
#removes excess characters before the string

def readFloat(file):
    return float(readString(file))

