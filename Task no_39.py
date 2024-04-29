
def count_string_vowel(names):
    vowels='AEIOUaeiou'
    count=0

    for name in names:
        if name[0] in vowels:
            print(name)
            count+=1
    
    return count



# Example usage:
names = ["Fahim", "Raheem", "Ihsan", "Ali", "Aftab", "Oil"]
result=count_string_vowel(names)
print("Number of names starting with a vowel:",result)