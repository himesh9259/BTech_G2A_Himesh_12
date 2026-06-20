# Transpose of a Matrix

matrix = [[1, 2, 3],
          [4, 5, 6]]

transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose Matrix:")
for row in transpose:
    print(row)
