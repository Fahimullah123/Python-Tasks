#  Write a program to check if a number is prime.


def is_prime(number):
    if number <= 1:
        return False  # 1 and numbers less than 1 are not prime
    if number <= 3:
        return True  # 2 and 3 are prime numbers

    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If it's divisible by any number, it's not prime
    return True

# Example usage:
num = 17
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

