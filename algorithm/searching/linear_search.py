def linear_seach(lst,num):

    for n in lst:
        if num == n:
            return True

    return False

lst = [1,2,3,4,5]
num = 10
print(linear_seach(lst,num))