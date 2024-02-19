"""

"""

"""
Method	       Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""

"""
1. capitalize()
Converts the first character of the string to uppercase.
"""
my_string = "Hello World"
casefolded_string = my_string.casefold()
print(casefolded_string)  # Output: "hello world"

"""
2. casefold()
Returns a casefolded copy of the string, suitable for caseless comparisons.
"""

my_string = "Hello World"
casefolded_string = my_string.casefold()
print(casefolded_string)  # Output: "hello world"

"""
3. center(width[, fillchar])
Returns a centered string of length width
"""
my_string = "hello"
centered_string = my_string.center(10, '-')
print(centered_string)  # Output: "--hello---"


"""
4. count(sub[, start[, end]])
Returns the number of occurrences of substring sub.
"""
my_string = "hello world"
count = my_string.count('l')
print(count)  # Output: 3

"""
5. encode(encoding="utf-8", errors="strict")
Returns an encoded version of the string.

"""
my_string = "hello world"
encoded_string = my_string.encode(encoding='utf-8')
print(encoded_string)  # Output: b'hello world'

"""
6. endswith(suffix[, start[, end]])
Returns True if the string ends with the specified suffix.
"""

my_string = "hello world"
ends_with = my_string.endswith('world')
print(ends_with)  # Output: True

"""
7. expandtabs(tabsize=8)
Expands tabs in a string to multiple spaces.
"""

my_string = "hello\tworld"
expanded_string = my_string.expandtabs()
print(expanded_string)  # Output: "hello   world"

"""
8. find(sub[, start[, end]])
Returns the lowest index of substring sub.
"""

my_string = "hello world"
index = my_string.find('o')
print(index)  # Output: 4

"""
9. format(*args, **kwargs)
Formats the string.

"""
my_string = "My name is {}, I'm {} years old"
formatted_string = my_string.format("Alice", 30)
print(formatted_string)  # Output: "My name is Alice, I'm 30 years old"

"""
10. format_map(mapping)
Formats the string using a mapping.
"""

my_string = "My name is {name}, I'm {age} years old"
formatted_string = my_string.format_map({"name": "Alice", "age": 30})
print(formatted_string)  # Output: "My name is Alice, I'm 30 years old"

"""
11. index(sub[, start[, end]])
Returns the lowest index of substring sub.
"""

my_string = "hello world"
index = my_string.index('o')
print(index)  # Output: 4

"""
12. isalnum()
Returns True if all characters in the string are alphanumeric.
"""

my_string = "hello123"
is_alnum = my_string.isalnum()
print(is_alnum)  # Output: True

"""
13. isalpha()
Returns True if all characters in the string are alphabetic.
"""

my_string = "hello"
is_alpha = my_string.isalpha()
print(is_alpha)  # Output: True


"""
14. isascii()
Returns True if all characters in the string are ASCII.
"""

my_string = "hello"
is_ascii = my_string.isascii()
print(is_ascii)  # Output: True

"""
15. isdecimal()
Returns True if all characters in the string are decimals
"""

my_string = "12345"
is_decimal = my_string.isdecimal()
print(is_decimal)  # Output: True

"""
16. isdigit()
Returns True if all characters in the string are digits.

"""
my_string = "12345"
is_digit = my_string.isdigit()
print(is_digit)  # Output: True

"""
17. isidentifier()
Returns True if the string is a valid identifier.
"""
my_string = "hello"
is_identifier = my_string.isidentifier()
print(is_identifier)  # Output: True

"""
18. islower()
Returns True if all characters in the string are lowercase.

"""
my_string = "hello"
is_lower = my_string.islower()
print(is_lower)  # Output: True

"""
19. isnumeric()
Returns True if all characters in the string are numeric.
"""

my_string = "12345"
is_numeric = my_string.isnumeric()
print(is_numeric)  # Output: True

"""
20. isprintable()
Returns True if all characters in the string are printable.
"""
my_string = "hello\nworld"
is_printable = my_string.isprintable()
print(is_printable)  # Output: False

"""
21. isspace()
Returns True if all characters in the string are whitespace.
"""

my_string = "   "
is_space = my_string.isspace()
print(is_space)  # Output: True

"""
22. istitle()
Returns True if the string is titlecased.
"""
my_string = "Hello World"
is_title = my_string.istitle()
print(is_title)  # Output: True

"""
23. isupper()
Returns True if all characters in the string are uppercase.

"""

my_string = "HELLO"
is_upper = my_string.isupper()
print(is_upper)  # Output: True

"""
24. join(iterable)
Joins the elements of an iterable with the string as a separator.
"""

my_list = ["hello", "world","hi"]
joined_string = "-".join(my_list)
print(joined_string)  # Output: "hello-world-hi"

"""
25. ljust(width[, fillchar])
Returns a left-justified string of length width.
"""

my_string = "hello"
left_justified_string = my_string.ljust(10, '-')
print(left_justified_string)  # Output: "hello-----"

"""
26. lower()
Converts all characters in the string to lowercase.
"""
my_string = "Hello World"
lowercase_string = my_string.lower()
print(lowercase_string)  # Output: "hello world"

"""
27 strip([chars]):
This method removes leading and trailing characters (whitespace characters by default) from both ends of a string.

lstrip([chars])
This method removes leading characters (whitespace characters by default) from the left side of a string.
rstrip([chars]):
This method removes trailing characters (whitespace characters by default) from the right side of a string
"""

my_string = "   hello world   "
stripped_string = my_string.strip()
print(stripped_string)  # Output: "hello world"

my_string = "   hello world   "
stripped_string = my_string.lstrip()
print(stripped_string)  # Output: "hello world   "

my_string = "   hello world   "
stripped_string = my_string.rstrip()
print(stripped_string)  # Output: "   hello world"

