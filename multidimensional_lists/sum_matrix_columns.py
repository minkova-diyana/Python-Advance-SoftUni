row, cow = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for i in range(row)]
# for j in range(cow):
#     sum_cow = 0
#     for i in range(row):
#         sum_cow += matrix[i][j]
#     print(sum_cow)
column_sums = [sum(matrix[i][j] for i in range(row)) for j in range(cow)]
print(*column_sums, sep='\n')
