my_list = [1, 3, 5, 8, 10]
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1
print("\n************\n")

"""
1. Using else with a While Loop:
You can combine a while loop with an else block, which will be executed when the loop terminates normally (i.e., the condition becomes false).
"""
count = 0
while count < 3:
    print("Inside the loop")
    count += 1
else:
    print("Loop execution complete")

"""
2. Handling User Input:
A while loop is useful for repeatedly prompting the user until valid input is provided.
"""

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        print("You entered:", int(user_input))
        break
    else:
        print("Invalid input. Please enter a valid number.")

"""

3. Using continue to Skip Iteration:
The continue statement skips the rest of the code inside the loop for the current iteration and continues with the next iteration.
"""


num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

"""
4. Infinite Loop with a Break Condition:
You can create a loop that runs indefinitely until a break condition is met.

while True:
    user_input = input("Enter a command (type 'exit' to quit): ")
    if user_input == 'exit':
        print("Exiting...")
        break
    else:
        print("Command:", user_input)
"""


while True:
    user_input = input("Enter a command (type 'exit' to quit): ")
    if user_input == 'exit':
        print("Exiting...")
        break
    else:
        print("Command:", user_input)

"""
5. Using else with Break:
You can use else with a while loop and a break statement to execute a block of code only 
if the loop completes without encountering a break
"""
num = 10
while num > 0:
    print(num)
    num -= 1
    if num == 6:
        break
else:
    print("Loop completed without encountering break.")
