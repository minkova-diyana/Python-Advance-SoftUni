from collections import deque
petrol_stops = int(input())
gas_and_distance = deque()
fuel = 0
count_rotation = 0
stops_count = 0
for _ in range(petrol_stops):
    petrol, destination_km = input().split()
    gas_and_distance.append([int(petrol), int(destination_km)])
while stops_count < petrol_stops:
    for i in range(petrol_stops):
        distance = gas_and_distance[i][1]
        fuel += gas_and_distance[i][0]
        if fuel < distance:
            gas_and_distance.rotate(-1)
            count_rotation += 1
            fuel = 0
            stops_count = 0
            break
        stops_count += 1
        fuel -= distance
print(count_rotation)
