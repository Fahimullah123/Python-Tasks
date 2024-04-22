# Create a function that takes a number as input and prints its multiplication table.

def multi_table(number):

    for i in range(1,10):
        print(number,"*",i,"=",number*i)


number=int(input("Enter number : "))

multi_table(number)