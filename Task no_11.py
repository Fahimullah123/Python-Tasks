#Create a program that takes a sentence as input and counts the number of words in it

def count_words(sentence):

    words=sentence.split()


    print("words is = ",words)

    return len(words)

sentence=input("Enter your sentence : ")

word=count_words(sentence)

print("The total number of words is : ",word)

