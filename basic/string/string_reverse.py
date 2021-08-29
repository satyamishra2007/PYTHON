def str_reverse(str):
    strArr = list(str)
    i = 0
    j = len(str)-1
    print(strArr)
    while i <=j:
        strArr[i],strArr[j] = strArr[j],strArr[i]
        i +=1
        j -=1

    return ''.join(strArr)

print(str_reverse("JAKE"))

