quantity_names = int(input())
names = set()
for _ in range(quantity_names):
    name = input()
    names.add(name)
set_name = set(names)
for n in set_name:
    print(n)