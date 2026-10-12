unit = int(input("Please enter number of units you consumed"))
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# check for units less than 100
elif(units <=100):
    amount = 130 +((units - 50) * 3.25)
    surcharge = 35

# check for units less than 200
elif(units <=200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# check for all the cases other than mentioned
# when units consumed are more that 200
elif(units <=100):
    amount = 130 + 162.50 + ((units - 200) * 8.45)
    surcharge = 75

# calculate and displaythe total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print("\nElecticity bill = "  ,total)
