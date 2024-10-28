n = int(input())

cars_in_parking = set()
for _ in range(n):
    command, car_number = input().split(', ')
    if command == 'IN':
        cars_in_parking.add(car_number)
    elif command == 'OUT':
        cars_in_parking.remove(car_number)

if cars_in_parking:
    print(*cars_in_parking, sep='\n')
else:
    print('Parking Lot is Empty')
