matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
transpose = []
for i in range(4):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print (transpose)

#In LIST comprehension

transposelistcomp = []

for i in range(4):
    transposelistcomp.append([row[i] for row in matrix])

print(transposelistcomp)


print([[row[i] for row in matrix] for i in range(4)])