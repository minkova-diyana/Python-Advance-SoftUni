n = int(input())
longest_intersection = set()
for _ in range(n):
    ranges = input().split('-')
    firs_start, firs_end = ranges[0].split(',')
    second_start, second_end = ranges[1].split(',')
    set_1 = set([num for num in range(int(firs_start), int(firs_end) + 1)])
    set_2 = set([num for num in range(int(second_start), int(second_end) + 1)])
    intersection = set_1 & set_2
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
