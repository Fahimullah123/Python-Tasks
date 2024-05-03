#Implement a program that takes a sentence and a word as 
#input and checks if the word is present in the sentence.

def check_word(sentence,word):

    sentence = sentence.lower()
    word= word.lower()
    words=sentence.split()

    if word in words:
        return True
    else:
        return False



sentence=input(" Sentence is : ")
word= input("Enter a Word : ")


if check_word(sentence,word):
    print(f"the {word} is present in sentence")
else:
    print(f"the {word} is not present in sentence")