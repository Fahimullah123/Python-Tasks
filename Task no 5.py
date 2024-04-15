#  Create a program that takes a user's name and age as 
#  input and prints a greeting message


#<--------- Solution ----------->


# create a function for greating message

def greating(name,age):

    print(f"Hello! {name} your are {age} year old")



name=input("Enter your Name = ")
age=input("Enter your Age : ")

greating(name,age)