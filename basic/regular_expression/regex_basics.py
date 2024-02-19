'''
https://www.programiz.com/python-programming/regex
'''

"""
The re module in Python provides support for working with regular expressions. It includes various functions and constants for pattern matching and manipulation of strings using regular expressions. Here's a summary of the functions and constants available in the re module:

Functions:
re.search(pattern, string, flags=0): Searches for a pattern in a string. Returns a match object if found, otherwise returns None.

re.match(pattern, string, flags=0): Attempts to match a pattern at the beginning of a string. Returns a match object if found, otherwise returns None.

re.findall(pattern, string, flags=0): Finds all occurrences of a pattern in a string and returns them as a list.

re.finditer(pattern, string, flags=0): Finds all occurrences of a pattern in a string and returns an iterator yielding match objects.

re.sub(pattern, repl, string, count=0, flags=0): Replaces occurrences of a pattern in a string with a replacement string.

re.split(pattern, string, maxsplit=0, flags=0): Splits a string by occurrences of a pattern.

re.compile(pattern, flags=0): Compiles a regular expression pattern into a regular expression object.

Match Object Methods:
group([group1, ...]): Returns one or more subgroups of the match.

start([group]): Returns the starting index of the match.

end([group]): Returns the ending index of the match.

span([group]): Returns a tuple containing the (start, end) indices of the match.

Constants:
re.IGNORECASE: Flag for case-insensitive matching.

re.MULTILINE: Flag for multiline matching, affecting the behavior of ^ and $.

re.DOTALL: Flag for dot (.) to match any character, including newline.

re.ASCII: Flag for ASCII-only matching.

re.UNICODE: Flag for treating the pattern and string as Unicode strings.

These are the main functions, methods, and constants available in the re module. Regular expressions are a powerful tool for pattern matching and text manipulation in Python.
"""

import re

# Example string
text = "The quick brown fox jumps over the lazy dog"

# 1. re.search()
match = re.search(r'fox', text)
if match:
    print("Found:", match.group())  # Output: Found: fox
else:
    print("Not found")

# 2. re.match()
match = re.match(r'The', text)
if match:
    print("Found:", match.group())  # Output: Found: The
else:
    print("Not found")

# 3. re.findall()
matches = re.findall(r'\b\w{4}\b', text)
print("All 4-letter words:", matches)  # Output: All 4-letter words: ['quick', 'brown', 'over', 'lazy']

# 4. re.finditer()
iterator = re.finditer(r'\b\w{4}\b', text)
for match in iterator:
    print("Match found at index", match.start(), ":", match.group())

# 5. re.sub()
new_text = re.sub(r'fox', 'cat', text)
print("After substitution:", new_text)  # Output: After substitution: The quick brown cat jumps over the lazy dog

# 6. re.split()
words = re.split(r'\s+', text)
print("Split words:",
      words)  # Output: Split words: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# 7. re.compile()
pattern = re.compile(r'\b\w{5}\b')
matches = pattern.findall(text)
print("All 5-letter words:", matches)  # Output: All 5-letter words: ['quick', 'brown']
