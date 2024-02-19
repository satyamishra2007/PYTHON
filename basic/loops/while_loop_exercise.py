# https://pythonistaplanet.com/python-while-loop-examples/

num = int(input("Enter a number to find factorial: "))

"""
Factorial of a given number using while loop
"""

i = 1
fact = 1
if num == 0:
    print(f"Factorial of Zero is {fact}")

elif num < 0:
    print("Factorial of -ve number cannot calculated .Please enter a positive number")

while i <= num:
    fact = fact * i
    i = i + 1

print(f"Factorial of given number is {fact}")
