from collections import deque
kids = deque(input().split())
number_tosses = int(input())
while len(kids) != 1:
    kids.rotate(-number_tosses + 1)
    print(f'Removed {kids.popleft()}')

print(f'Last is {kids.pop()}')
