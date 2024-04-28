
#  Write a Python program to find the length of the longest word in a sentence
def lon_word(sentence):
    words=sentence.split()

    longest_word=0


    for word in words:
        if len(word)> longest_word:
            longest_word=len(word)

    return longest_word




sentence = "The quicksss brown fox jumps over the lazy dog"
result=lon_word(sentence)
print(result)