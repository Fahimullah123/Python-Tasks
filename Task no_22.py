# Implement a program that converts a given number of minutes into hours and minutes

def con_num_time(number):

    hours=number/60
    mint=hours*60


    return hours,mint

num=int(input("Enter any number : "))

hours,mint=con_num_time(num)

print("Hours is : ",hours)
print("Mintus is : ",mint)


