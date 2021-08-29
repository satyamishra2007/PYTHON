from collections import OrderedDict

seq = ['aaa','bbb','ccc','ddd','aaa','aaa','bbb']
count_map = {}

population = {"china":100 ,"india":95,"europe":90,"usa":80, "aus": 70}


















def MaxPopulation(map):
    max_cntry =  max(map,key=map.get)
    return max_cntry

def usingCollection(map):
     result_dict = OrderedDict(sorted(map.items()))
     return result_dict

def usingSortMethod(map):
    return dict(sorted(map.items()))

def usingSortMethodByValue(map):
    return dict(sorted(map.items(),key = lambda kv : kv[1],reverse=True))

print("using collection dictionary sort by key" ,usingCollection(population))
print("using sort method by key" ,usingSortMethod(population))
print("using sort method by val" ,usingSortMethodByValue(population))
print("MAX population :" ,MaxPopulation(population))



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

