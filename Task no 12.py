#Implement a program that swaps the values of two variables.

def swapping_value(a,b):

    print("Before swapping")
    print("a : ",a)
    print("b : ",b)

    #swapping value is

    a,b=b,a

    print("After Swapping")

    print("a : ",a)
    print("b : ",b)



a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))

swapping_value(a,b)