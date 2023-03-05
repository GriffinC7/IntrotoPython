def printHeading():
    print("\nTotal\tAverage")
    
def printDetail (total, average):
    print(total,"\t", average)

def main()
    total = 0.0
    count = 0
    value = float(input("Enter a positive number (0 to end): "))

    while value != 0:

        while value < 0:
            print("number entered must be positive.")
            value = float(input("Enter a positive number: ")

        total += value
        count += 1
        value = float(input("Enter a positive number (0 to end): "))

     if count > 0:
        printHeading()
        print(total "\t", total/count, sep='')
        printDetail()


#invoke "main"
main()

            
                          

        
                    
                          
        
