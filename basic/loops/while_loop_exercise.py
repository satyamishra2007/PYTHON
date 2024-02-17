
# https://pythonistaplanet.com/python-while-loop-examples/

a = 'geeksforgeeks'
i = 0
# while i < len(a):
#      if a[i] == 'e' or a[i] == 's':
#          continue
#      i += 1
#      print("Array Elements:",a[i])



'''
Factorial of a given number using while loop
'''

num = int(input("Enter a number to find factorial: "))

i = 1
fact = 1
if num ==0:
    print(f"Factorial of Zero is {fact}")

elif num < 0:
    print("Factorial of -ve number cannot calculated .Please enter a positive number")


while i <= num:
    fact = fact * i
    i = i + 1

print(f"Factorial of given number is {fact}")