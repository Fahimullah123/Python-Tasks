#Create a program that takes a temperature in Celsius and converts it to Kelvin

def cel_to_kel(celsius):

    return celsius+273.15

celsius=float(input("Enter Temperature in Celsius : "))

kelven=cel_to_kel(celsius)

print("Temperature into kelven is : ",kelven)

