def even(numbers):
    return numbers % 2 == 0


list_numbers = [int(numbers) for numbers in input().split()]
even_list = list(filter(even, list_numbers))
print(even_list)
