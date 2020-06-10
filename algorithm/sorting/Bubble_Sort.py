"""

"""
"""
Bubble Sort
Time Complexity: O(n2) 
Space Complexity: O(1)

https://www.geeksforgeeks.org/bubble-sort/
"""


def bubble_sort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(l - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


print(bubble_sort([6, 3, 7, 1, 9, 2, ]))