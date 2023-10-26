## No takey my code. is mine
print("US dollar to Euro converter")
print("Made by Mudshoes. All rights reserved. 2023")
print("Prints amount in euros when given a US dollar amount")
print("Warning: Only the US dollar or currencies of equal value will have accurate conversions!")

## When answer = no or 0, the while loop stops
answer = 'yes'
while True:
    ## Gets the dollar amount from the user
    dollar = float(input("How many dollars are there?"))

    ##converts dollars to euros
    euro = dollar * 0.94540

    ## Prints the amount of euros
    print("Euros: " + str(euro))

    answer = input("Continue conversions?")
    if answer == 'no' or '0' or 'n':
        break