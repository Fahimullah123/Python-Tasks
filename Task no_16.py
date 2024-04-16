#Given a list of numbers, find the sum and average


def sum_average(List):

    total_sum= sum(List)
    average=total_sum/len(List)


    return total_sum,average



List =[12,23,43,54,65,23,54,23,54,23]

sum,average=sum_average(List)
print("The sum is : ",sum)
print("The average is : ",average)
