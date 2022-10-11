year = int(input('Enter year : '))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0) : print(year, "is a leap year.")
else :print(year, "is not a leap year.")

cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))

# DID THE OPTIONAL ALSO *^____^*
