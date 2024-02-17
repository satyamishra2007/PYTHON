# Binary Search in python


def binarySearch(array, x):

    low = 0
    high = len(array)-1

    while low < high:

        mid = (low + high)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


class Solution:
    def search(self, nums, target):
        l = len(nums)
        low = 0
        high = l - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

array = [3, 4, 5, 6, 7, 8, 9,11]
x = 9
print("Binary Search: ",Solution().search(array,x))

