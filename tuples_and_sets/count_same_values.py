numbers = tuple(float(num) for num in input().split())
checker = []
for number in numbers:
    if number not in checker:
        print(f'{number} - {numbers.count(number)} times')
    checker.append(number)
