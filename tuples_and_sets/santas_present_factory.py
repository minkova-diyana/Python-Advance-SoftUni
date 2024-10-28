from collections import deque


def successful_crafting(presents):
    return ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents)


crafting_materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
magic_for_present = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = {}
while crafting_materials and magic_levels:
    material = crafting_materials.pop()
    magic = magic_levels.popleft()
    if magic == 0 and material == 0:
        continue
    elif magic == 0:
        crafting_materials.append(material)
        continue
    elif material == 0:
        magic_levels.appendleft(magic)
        continue
    total_magic = magic * material
    if total_magic < 0:
        new_material = magic + material
        crafting_materials.append(new_material)
    elif total_magic in magic_for_present:
        key = magic_for_present[total_magic]
        if key not in crafted_presents:
            crafted_presents[key] = 0
        crafted_presents[key] += 1
    else:
        material += 15
        crafting_materials.append(material)
if successful_crafting(crafted_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if crafting_materials:
    print(f'Materials left: {", ".join([str(m) for m in crafting_materials[::-1]])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(l) for l in magic_levels])}')

for toy, count in sorted(crafted_presents.items()):
    if count > 0:
        print(f'{toy}: {count}')
