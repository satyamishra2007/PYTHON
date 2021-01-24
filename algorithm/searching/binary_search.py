# BINARY SEARCH TREE

"""
-- Works on sorted array

Time complexity : O(N)
Space Complexity :  O(1)

"""


#
# def binary_search(item_list, item):
#     first = 0
#     last = len(item_list) - 1
#     found = False
#     while (first <= last and not found):
#         mid = (first + last) // 2
#         if item_list[mid] == item:
#             found = True
#         else:
#             if item < item_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found




def binary_search(arr ,num):
    low = 0
    high = len(arr) - 1
    mid = 0
    while (low <= high):
        mid = (low + high)//2
        if arr[mid] < num :
            low = mid + 1
        elif arr[mid] > num:
            high = mid -1
        else:
            return mid
    return -1




print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))

