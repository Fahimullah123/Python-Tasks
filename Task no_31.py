 # Create a function to find the square of each element in a given list


sqre=[]

def sqr_no(list):

    for i in list:
        sqre.append(i**2)

    return sqre


list=[1,5,4,8,9,3,8,7]
print("orgnail : ",list)
print("sqr list : ",sqr_no(list))