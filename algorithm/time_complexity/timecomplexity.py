

"""
Time Complexity :

1.Keep the fastest growing term
2.Drop constants

time vs size(arr) --Linear growth

Worst : BigO
Best : 
Average:

"""
##O(1)


def get_stock_price(cmpny):
    stock_prices = {"apple": 200, "facebook": 180, "amazon": 300}
    return stock_prices[cmpny]

print(get_stock_price("apple"))



##O(n)

def get_squared_number(nums):
    squared_num = []
    for n in nums:
        squared_num.append(n * n)
    return squared_num

nums = [1,2,3,4]
print(get_squared_number(nums))

##O(n2)

numbers = [ 3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], " is a duplicate")
            break
