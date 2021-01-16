emptySet=set()
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