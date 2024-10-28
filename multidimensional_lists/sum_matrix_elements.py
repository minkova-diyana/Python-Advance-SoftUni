row, cow = [int(x) for x in input().split(', ')]
matrix = []
sum_matrix = 0
for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])
for r_index in range(row):
    for c_index in range(cow):
        sum_matrix += matrix[r_index][c_index]
print(sum_matrix)
print(matrix)