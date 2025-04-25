def find_the_sum(special_number):
    is_perfect = True
    list_numbers = []
    for number in range(1, special_number):
        if special_number % number == 0:
            list_numbers.append(number)
    if sum(list_numbers) != given_number:
        is_perfect = False
    return is_perfect


given_number = int(input())

perfect_number = find_the_sum(given_number)

if perfect_number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")

