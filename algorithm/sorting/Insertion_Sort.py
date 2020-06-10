"""

"""
"""
### Insert Sort

Time Complexity: O(n2)
Space Complexity: O(1)
https://www.geeksforgeeks.org/insertion-sort/

"""


def insert_sort(lst):
    l = len(lst)
    for i in range(1, l):
        j = i - 1
        key = lst[i]
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


print(insert_sort([6, 3, 7, 1, 9, 2]))

