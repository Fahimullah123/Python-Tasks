#  Q 1:  Write a program that checks if a given number is positive, negative, or zero.

def check_number(num):

    if num==0:
        print("That i zero")
    elif num>0:
        print("That is positive number")
    else:
        print("That is Negative number")



num=int(input("Enter Any Number : "))

#calling the function
check_number(num)