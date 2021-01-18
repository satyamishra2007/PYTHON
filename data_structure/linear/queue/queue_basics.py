#FIF)

from collections import deque

queue = deque(['satya','mishra','jeypore','swati','mishra','puri'])


#Traverse
for val in queue:
    print(val)

# print('***************')
# for i in range(len(queue)):
#     print(queue[i])


#push
print('***************')
queue.append("USA")
for val in queue:
    print(val)


#pop

print('***************')
queue.popleft()
for val in queue:
    print(val)

print('***************')
queue.pop()
for val in queue:
    print(val)
