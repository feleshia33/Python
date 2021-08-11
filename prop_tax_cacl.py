# This program ask the user for their actual value of a piece of property
# and displays the assessment value and propery tax

A_VALUE = .60
PROP_TAX = .72


value_land = float(input("Enter the land/property value: "))
value = float(value_land * A_VALUE)
print("The assesment value of land is", value)
prop_tax_calc = ((value * PROP_TAX) / 100)
print("The property tax land is", prop_tax_calc)
