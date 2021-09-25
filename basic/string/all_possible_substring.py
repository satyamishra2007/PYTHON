def all_possible_substring(str):
    res = []
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            res .append(str[i:j])

    return res

print(all_possible_substring("geeksforgeeks"))


