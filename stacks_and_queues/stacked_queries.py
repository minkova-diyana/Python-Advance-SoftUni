number_rotations = int(input())
stack = []
for number in range(number_rotations):
    commands = input().split(' ')
    if len(commands) > 1:
        stack.append(int(commands[1]))
    elif len(stack) >= 1:
        if commands[0] == '2':
            stack.pop()
        elif commands[0] == '3':
            print(max(stack))
        elif commands[0] == '4':
            print(min(stack))

print(', '.join(reversed([str(string)for string in stack])))
