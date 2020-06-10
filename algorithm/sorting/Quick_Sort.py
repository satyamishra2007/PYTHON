"""

"""

"""
### Quick Sort 

Time Complexity: O(n log(n))
Space Complexity: O(n)
https://www.geeksforgeeks.org/quick-sort/
"""


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(i)
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


arr = [6, 3, 7, 1, 9, 2]
low = 0
high = len(arr) - 1
print(quickSort(arr, low, high))