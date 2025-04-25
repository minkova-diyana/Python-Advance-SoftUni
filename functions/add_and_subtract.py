def sum_numbers(first, second):

    return first + second


def subtract(add, third):

    return add - third


def add_and_subtract(one, two, three):
    add_sum = sum_numbers(one, two)
    result = subtract(add_sum, three)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))