def list_digits(given_number):
    return [int(digit) for digit in given_number]


def odd_even(list_numbers):
    odd_num = [digit for digit in list_numbers if digit % 2 != 0]
    even_num = [digit for digit in list_numbers if digit % 2 == 0]

    return odd_num, even_num


number = input()
odd, even = odd_even(list_digits(number))

print(f'Odd sum = {sum(odd)}, Even sum = {sum(even)}')
print(odd)
print(even)
