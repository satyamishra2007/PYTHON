def uniqueChars_map(str):
    map = {}
    isUnique = True
    for c in str:
        if c in map:
            map[c] += 1
        else:
            map[c] =1

    for v in map.values():
        if v > 1:
            isUnique = False
    if isUnique:
        return True
    else:
        return False

def uniqueChars_set(str):
    uniquechars = set(str)

    if len(str) == len(uniquechars):
        return True
    else:
        return False



def uniqueChars_without_another_DS(str):

    checker = 0
    for c in str:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0 :
            return False
        checker |=(1 << val)
    return True






s = 'abcdc'
print("uniqueChars_map:",uniqueChars_map(s))
print("uniqueChars_set:",uniqueChars_set(s))
print("uniqueChars_without_another_DS:",uniqueChars_without_another_DS(s))
