## No takey my code. is mine
## prints name, credits, instuctions, and warnings.
print("US dollar to Euro converter")
print("Made by Mudshoes. All rights reserved. 2023")
print("Prints amount in euros when given a US dollar amount")
print("Warning: Only the US dollar or currencies of equal value will have accurate conversions!")

## When answer = no or 0, the while loop stops
answer = 'yes'
while True:
    ## Gets the dollar amount from the user
    dollar = float(input("Enter dollar amount to be converted: "))

    ##converts dollars to euros
    euro = dollar * 0.94540

    ## Prints the amount of euros
    print("Euros: " + str(euro))
    
    '''
    Asks if the user would like to continue.
    If the answer is "no", "0", or "n" it breaks the loop
    Otherwise the loop continues.
    '''
    answer = input("Would you like to convert dollars to euros? ")
    if answer == 'no' or '0' or 'n':
        break