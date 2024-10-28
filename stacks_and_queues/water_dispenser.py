from collections import deque
quantity_water = int(input())
que_line = deque()
names = input()
while names != 'Start':
    que_line.append(names)
    names = input()
command = input()
while command != 'End':
    command = command.split()
    if len(command) > 1:
        quantity_water += int(command[1])
    else:
        liters_to_give = int(command[0])
        if liters_to_give <= quantity_water:
            print(f'{que_line.popleft()} got water')
            quantity_water -= liters_to_give
        else:
            print(f'{que_line.popleft()} must wait')
    command = input()
print(f'{quantity_water} liters left')
