# Q4: Write a Python program to calculate the area of a 
#       rectangle given its length and width

# Formulat->  Area=Width* Height


# create Function

def find_area(length,width):

    area=length*width
    return area


length=float(input("Enter length of Area : "))
width = float(input("Enter width of Area : "))

area= find_area(length,width)

print("The Total Area is : ", area)