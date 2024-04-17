# Write a Python program to check if a given string is a 
# pangram (contains all letters of the alphabet)

import string

def is_pangram(input_string):
    # Create a set of lowercase letters
    alphabet = set(string.ascii_lowercase)
    
    # Convert input string to lowercase and remove non-alphabetic characters
    input_string = input_string.lower()


        
    input_string = ''.join(char for char in input_string if char.isalpha())
    # Check if all letters in the alphabet are present in the input string
    return set(input_string) == alphabet

# Example usage:
input_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(input_str))  # Output: True