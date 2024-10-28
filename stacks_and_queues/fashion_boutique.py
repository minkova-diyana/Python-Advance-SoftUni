stack_of_boxes = [int(clothes) for clothes in input().split()]
rack_capacity = int(input())
count_racks = 1
rack = rack_capacity
while stack_of_boxes:
    clothing = stack_of_boxes.pop()
    if clothing <= rack:
        rack -= clothing
    else:
        rack = rack_capacity
        count_racks += 1
        rack -= clothing
print(count_racks)