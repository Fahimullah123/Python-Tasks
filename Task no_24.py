#  Write a program to check if a number is prime.


def check_number(number):

    if number%2==0:
        print("That is Even Number : ",number)
    else:
        print("That is Odd Number : ",number)

number=int(input('Enter Any Number : '))


#call the function
check_number(number)


