
a = 'geeksforgeeks'
i = 0
while i < len(a):
     if a[i] == 'e' or a[i] == 's':
         continue
     i += 1
     print("Array Elements:",a[i])