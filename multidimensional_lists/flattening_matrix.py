row = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]
#flatted = [j for row in matrix for j in row]
flatted = []
for row in matrix:
    for c in row:
        flatted.append(c)
print(flatted)