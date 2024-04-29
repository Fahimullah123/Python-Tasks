
def remove_duplicates(input_string):
    # Initialize an empty set to keep track of unique characters
    seen = set()
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character has not been encountered before
        if char not in seen:
            # If not, add it to the result and mark it as seen
            result += char
            seen.add(char)
    
    return result

# Example usage:
input_string = "hello"
print(remove_duplicates(input_string))  # Output: "helo"
