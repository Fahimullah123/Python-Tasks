# Q 10: Given a list of integers, find the sum of all positive numbers


def sum_of_list(list):

    for i in list:

        sum= sum+i

        return sum
    

list=[45,8,6,8,64,95,1]

result=sum_of_list(list)

print("The sum of is : ",sum)