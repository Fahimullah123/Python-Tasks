# Given a string, write a function to remove all vowels from it and return 
# the modified string

def remove_vow(sen):
    char=[]
    vowels="aeiouAEIOU"

    for i in sen:
        if i not in vowels:
            char.append(i)

    return char
    #return ''.join([i for i in sen if i not in vowels ])



sentence="Hello This is Fahim"

result=remove_vow(sentence)
print(result)