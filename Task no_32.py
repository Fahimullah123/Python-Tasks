#Write a function that takes two lists and returns their intersection (common elements)



def intersection(fist_list,sec_list):
    intersection_list=[]
    for i in fist_list:
        if i in sec_list and i not in intersection_list:
            intersection_list.append(i)

    return intersection

fist_list=[1,3,4,2,6,5,8,9,7]
sec_list=[3,4,10,5,12,18,7,1,13]
result=intersection(fist_list,sec_list)
print(result)
