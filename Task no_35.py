#  Write a program that takes a sentence as input and counts the number of words in it

def count_words(sentence):
    word_list = sentence.split()
    num_words = len(word_list)
    return num_words

# Example usage:
input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print("Number of words:", word_count)
