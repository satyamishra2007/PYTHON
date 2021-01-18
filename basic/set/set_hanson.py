emptySet=set()

my_set = {1, 3, 4, 5, 6}
my_set.add(7)
my_set.discard(4)
print(my_set)
#my_set.discard(4)
my_set.remove(4)
print(my_set)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(emptySet,basket)

a = set('abracadabra')
b = set('alacazam')
print(a-b)
print(a|b)
print(a&b)
print(a ^ b)


setComp = {x for x in a if x not in 'abc'}
print(setComp)