seq = ['aaa','bbb','ccc','ddd','aaa','aaa','bbb']
count_map = {}

def secondLargest(seq):
    for s in seq:
        if s in count_map.keys():
            count_map[s] += 1
        else:
            count_map[s] = 1

    max_value = max(count_map.values())
    max2 = 0

    for k in count_map:
        if count_map[k] == max_value:
            print("Largest Value with Key",k)

    for k in count_map:
        if count_map[k] < max_value and count_map[k] > max2:
            max2 = count_map[k]
            key = k
    print("2nd largest",key)


secondLargest(seq)

