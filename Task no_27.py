# Q 3: Implement a program that finds the largest number in a list.


def find_greater(List):
    max_num=List[0]
    for i in List:
        if i > max_num:
            max_num=i
    return max_num

List=[15,10,21,45,87,99,100,25,44]


Greater_value=find_greater(List)
print("The greater value is : ",Greater_value)