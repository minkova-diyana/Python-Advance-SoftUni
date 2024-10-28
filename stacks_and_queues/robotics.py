from datetime import datetime, timedelta
from collections import deque
info = [x.split('-') for x in input().split(';')]
robots_time = {k: v for k, v in info}
hours, minutes, seconds= [int(unit)for unit in input().split(':')]
start_time = datetime.now().replace(hour=hours, minute=minutes, second=seconds)
products = deque()
time_tabel = {}
while True:
    p = input()
    if p == 'End':
        break
    products.append(p)
for robot, time in robots_time.items():
    product = products.popleft()
    start_time += timedelta(seconds=1)
    time_tabel[robot] = start_time + timedelta(seconds=int(time))
    print(f'{robot} - {product} [{start_time.time().strftime("%H:%M:%S")}]')

while products:
    products.rotate(-1)
    for bot, t in sorted(time_tabel.items(), key=lambda x:x[1]):
        product = products.popleft()
        print(f'{bot} - {product} [{t.strftime("%H:%M:%S")}]')
        time_tabel[bot] = t + timedelta(seconds=int(robots_time[bot]))
        if not product:
