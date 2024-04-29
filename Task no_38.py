# Create a function that takes a sentence as input and returns the sentence in reverse order

def reverse_word(word):
    return word[::-1]  # Reverses the characters in the word

def reverse_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = [reverse_word(word) for word in words]  # Reverse each word
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words back into a sentence
    return reversed_sentence

# Example usage:
sentence = "Hello world! This is a test."
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
