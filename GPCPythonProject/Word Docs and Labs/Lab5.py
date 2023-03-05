#Lab 5 Generating payment based packages sold by a Software company

Packages_Sold = int(input('Number of Packages purchased: '))
Price = Float(99.00)

#Processing
Quantity_Ordered = Packages_Sold

if Quantity_Ordered >= 10 and Quantity_Ordered < 20
    print(Discount_Percent = 10%)
    
if Quantity_Ordered >= 20 and Quantity_Ordered < 50
    print(Discount_Percent = 20%)
    
if Quantity_Ordered >= 50 and Quantity_Ordered <= 99
    print(Discount_Percent = 30%)
    
if Quantity_Ordered >= 100
    print(Discount_Percent = 40%)
   
Order Total = float(Quantity_Ordered * Price)
Less_Discount = Float(Discount_Percent * Order_Total)
AmountDue = Float(Order_Total - Less_Discount)

print("Packages_Sold")
