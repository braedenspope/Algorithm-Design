# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      Prompt the user for a number, and calculates all numbers at or below the given number.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was understanding how to iterate through all the numbers in the most
#      efficent way, by not double checking certain values.
# 5. How long did it take for you to complete the assignment?
#      2 hours

# Import square root function.
from math import sqrt

# Prompts the user for a number greater than 2 to calculate the primes at or under.
import numbers
number = int(input("This program will find all the prime numbers at or below N. Select that N: "))
while (number < 2):
    number = int(input("The number must be greater than 2. Select that N: "))

# Creates the array of boolean values for the numbers, primes, and sets 0 and 1 as prime numbers.
numbers = [True for x in range(0, number + 1)]
assert len(numbers) == number + 1, "array has wrong length"
numbers[0] = False
numbers[1] = False
primes = []

# Calculates the prime numbers at or under the given number by counting multiples of the numbers under the
# square root of the given number.
for factor in range(2, int(sqrt(number)) + 1):
    assert factor < int(sqrt(number) + 1), "incorrect number of iterations"
    if (numbers[factor]):
        for multiple in range(factor * 2, number + 1, factor):
            assert multiple % factor == 0, "doesn't step with the factor variable"
            numbers[multiple] = False

# Adds all prime numbers to the prime array.
for index in range(2, number + 1):
    if (numbers[index]):
        primes.append(index)

# Displays the prime numbers to the user.
print(f"The prime numbers at or below {number} are {primes}")