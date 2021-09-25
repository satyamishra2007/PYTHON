

"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = { "brand": "Ford", "model": "Mustang","year": 1964 }
print(thisdict)

Properties :
- Keys are unique in nature

"""

#https://www.programiz.com/python-programming/methods/dictionary/copy
"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

#EMPTY Dictionary declaration
my_dict = {}
mydict = dict()

print(my_dict,mydict)


#adding element

my_dict[1] = "CA"
my_dict[2] = "AZ"
my_dict[3] = "OH"
my_dict[4] = "FL"

mydict  = {1:"CA",2:"AZ",3:"OH",4:"FL"}
print(my_dict,"\n",mydict)


#traveresing keys

# for key in mydict.keys():
#     print(key)
#
#
# for val in mydict.values():
#     print(val)

for k,v in mydict.items():
    print(k,v)

print(mydict.get(1,"NO STATE"))
print(mydict[1])
# print(mydict.popitem())
# print(mydict.pop(2))
# print(mydict)





##NESTED dictionaries


people = {1:{'name':'john','age':12,'sex':'male'},
          2:{'name':'marie','age':18,'sex':'female'}}
print(people[1],people[2])
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3] = {'name':'robin','age':32,'sex':'male','married':'no'}

people[4] = {}
people[4]['name'] = 'sat'
people[4]['age'] = 30
people[4]['sex'] = 'male'
people[4]['married'] = 'yes'
print(people)


##Traversing nested distionary

for p_key,p_val in people.items():
    print("\nPerson ID :",p_key)
    for k in p_val:
        print(k + ":" ,p_val[k])

## Deleting elements

del people[3]
del people[4]['married']
people.pop(2)
people.popitem()
print(people)

#vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)