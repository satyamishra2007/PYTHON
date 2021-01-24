arr = [1,3,5,8,10]
i =0
l = len(arr)
while i < l:
    print(arr[i])
    i += 1



list1 = [1,2,3]
list2 = [5,7,8,9]

result = []
l = len(list1)
r = len(list2)

def mergeList (l1,l2):

    l = len(l1)
    r = len(l2)
    i =j = k = 0
    result = list(range(l+r))
    while i < l and j < r:
        if l1[i] < l2[j]:
            result[k] = l1[i]
            i +=1
        else:
            result[k] = l2[j]
            j +=1
        k +=1

    while i < l:
        result[k] = l1[i]
        i +=1
        k +=1
    while j < r:
        result[k] = l2[j]
        j +=1
        k +=1
    return  result


print(mergeList(list1,list2))




