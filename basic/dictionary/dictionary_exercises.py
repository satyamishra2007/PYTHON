l1 = ['satya', 'swati','rohan']
l2 = [34, 31, 7]


print(tuple(zip(l1,l2)))



# adding element

my_dict[1] = "CA"
my_dict[2] = "AZ"
my_dict[3] = "OH"
my_dict[4] = "FL"

mydict = {1: "CA", 2: "AZ", 3: "OH", 4: "FL"}
print(my_dict, "\n", mydict)

# traveresing keys

# for key in mydict.keys():
#     print(key)
#
#
# for val in mydict.values():
#     print(val)

for k, v in mydict.items():
    print(k, v)

print(mydict.get(1, "NO STATE"))
print(mydict[1])
# print(mydict.popitem())
# print(mydict.pop(2))
# print(mydict)


# NESTED dictionaries


people = {1: {'name': 'john', 'age': 12, 'sex': 'male'},
          2: {'name': 'marie', 'age': 18, 'sex': 'female'}
          }
print(people[1], people[2])
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3] = {'name': 'robin', 'age': 32, 'sex': 'male', 'married': 'no'}

people[4] = {}
people[4]['name'] = 'sat'
people[4]['age'] = 30
people[4]['sex'] = 'male'
people[4]['married'] = 'yes'
print(people)

# Traversing nested distionary

for p_key, p_val in people.items():
    print("\nPerson ID :", p_key)
    for k in p_val:
        print(k + ":", p_val[k])

# Deleting elements

del people[3]
del people[4]['married']
people.pop(2)
people.popitem()
print(people)

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
