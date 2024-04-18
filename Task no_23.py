#Create a function to count the number of vowels in a given string

def find_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in string:
        if i in vowels:
            count=count+1
    return count


string="Hellow this is fahim"
counts=find_vowels(string)
print("The number of vowels is :  ",counts)