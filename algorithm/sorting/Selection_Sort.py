
"""
### Selection Sort

Time Complexity: O(n2)
Space Complexity: O(1)
https://www.geeksforgeeks.org/selection-sort/


"""


def selection_sort(lst):
    l = len(lst)
    for i in range(l):
        min_idx = i
        for j in range(i + 1, l):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


print(selection_sort([6, 3, 7, 1, 9, 2, ]))
