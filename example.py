from collections import deque

crafting_materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
points = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = {}

while crafting_materials and magic_levels:
    total_magic = crafting_materials[-1] * magic_levels[0]
    if total_magic in points:
        key = points[total_magic]
        if key not in crafted_presents:
            crafted_presents[key] = 0
        crafted_presents[key] += 1
        crafting_materials.pop()
        magic_levels.popleft()
    elif total_magic < 0:
        crafting_materials.append(crafting_materials.pop() + magic_levels.popleft())
    elif total_magic > 0:
        magic_levels.popleft()
        crafting_materials[-1] += 15
    elif crafting_materials[-1] == 0 and magic_levels[0] == 0:
        crafting_materials.pop()
        magic_levels.popleft()
    elif crafting_materials[-1] == 0:
        crafting_materials.pop()
    elif magic_levels[0] == 0:
        magic_levels.popleft()

if ('Doll' and 'Wooden train' in crafted_presents) or ('Teddy bear' and 'Bicycle' in crafted_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if crafting_materials:
    print(f'Materials left: {", ".join([str(x) for x in crafting_materials[::-1]])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(x) for x in magic_levels])}')

for toy, count in sorted(crafted_presents.items()):
    if count > 0:
        print(f'{toy}: {count}')