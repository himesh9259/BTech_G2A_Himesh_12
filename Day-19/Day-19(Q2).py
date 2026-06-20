# Matrix Subtraction

A = [[7, 8, 9],
     [4, 5, 6]]

B = [[1, 2, 3],
     [1, 2, 3]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    result.append(row)

print("Difference of matrices:")
for row in result:
    print(row)
