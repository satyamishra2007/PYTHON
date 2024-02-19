"""

"""

"""
In Python, you can perform file operations using various modes. Here are the common file modes along with examples:
"""
with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file \n")
    f.write("This file \n")
    f.write("contains three lines \n")
    f.close()

with open("test.txt", 'r') as f1:
    f1_list = f1.readlines()
    result = []
    for line in f1_list:
        result.append(line.split())
print(f"result:{result}")

"""
1. Read Mode ('r'):
Open the file for reading. The file pointer is placed at the beginning of the file
"""

# Open a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

"""
2. Write Mode ('w'):
Open the file for writing. If the file exists, its contents are overwritten. If the file does not exist, a new file is created
"""

# Open a file in write mode
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

"""
3. Append Mode ('a'):
Open the file for appending. The file pointer is placed at the end of the file. New data is written to the end of the file.
"""

# Open a file in append mode
with open('example.txt', 'a') as file:
    file.write("\nAppending additional content.")

"""
4. Read and Write Mode ('r+'):
Open the file for reading and writing. The file pointer is placed at the beginning of the file.
"""

# Open a file in read and write mode
with open('example.txt', 'r+') as file:
    content = file.read()
    print("Before writing:", content)

    # Move the file pointer to the beginning
    file.seek(0)

    # Write additional content
    file.write("Additional content written in read and write mode.\n")

    # Move the file pointer to the beginning
    file.seek(0)

    # Read the updated content
    updated_content = file.read()
    print("After writing:", updated_content)

"""
5. Write and Read Mode ('w+'):
Open the file for reading and writing. If the file exists, its contents are overwritten. If the file does not exist, a new file is created.

"""

# Open a file in write and read mode
with open('example.txt', 'w+') as file:
    file.write("Writing and reading in write and read mode.\n")
    file.seek(0)
    content = file.read()
    print(content)

"""
6. Binary Mode ('b'):
Add 'b' to the mode to open the file in binary mode (e.g., 'rb', 'wb', 'ab', 'r+b', 'w+b').
"""

# Open a file in binary read mode
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)
