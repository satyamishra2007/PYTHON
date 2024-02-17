import timeit

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
    return str(stock_prices[cmpny])


call = timeit.timeit(get_stock_price("apple"))
print(f"Time Taken {call}")


def sum_of_n_numbers1(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


def sum_of_n_numbers2(n):
    return (n * (n+1) // 2)


print(f"Time Taken For Sum1 {timeit.timeit(str(sum_of_n_numbers1(100000)))}")

print(f"Time Taken For Sum2 {timeit.timeit(str(sum_of_n_numbers2(100000)))}")
