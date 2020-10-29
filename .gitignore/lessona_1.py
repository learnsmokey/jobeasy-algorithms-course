# Homework: Rewrite a program with any number of digits.
# Instead of  3 digits, you should sum digits up from n digits number,
# Where User enter n manually. n > 0

from random import randint

# Get the number of digits using input

n = int(input("Input number of digits to sum up? "))
result = 0
if (n <= 0):
    print("Enter valid number above zero")
else:
    smallest = (10**(n-1))
    largest = ((10**n)-1)
    randomNumber = randint(smallest,largest)
    print(randomNumber)
    while ( randomNumber % 10):
        result += (randomNumber % 10)
        randomNumber = randomNumber//10
    print(result)