n = int(input())
reservations = set()
for _ in range(n):
    reserved_guest = input()
    reservations.add(reserved_guest)

guest = input()
while guest != 'END':
    reservations.remove(guest)
    guest = input()

print(len(reservations))
print(*sorted(reservations), sep='\n')
