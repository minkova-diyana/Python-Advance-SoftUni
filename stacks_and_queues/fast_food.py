from collections import deque
quantity_food = int(input())
que_line = deque(int(order) for order in input().split())
print(max(que_line))
while que_line:
    food_to_serve = que_line.popleft()
    if quantity_food >= food_to_serve:
        quantity_food -= food_to_serve
    else:
        que_line.appendleft(food_to_serve)
        break
if que_line:
    print(f"Orders left: {' '.join(str(orders) for orders in que_line)}")
else:
    print('Orders complete')
