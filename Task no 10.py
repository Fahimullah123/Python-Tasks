# Q 10: Given a list of integers, find the sum of all positive numbers



def sum_of_positive(list):

    sum=0

    for i in list:
        if i>0:
            sum=sum+i


    return sum
   

list=[-45,8,-6,10,-64,95,1]

result=sum_of_positive(list)

print("The sum of the list is : ", result)


