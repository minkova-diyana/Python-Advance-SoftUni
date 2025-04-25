def find_characters_between(one, two):
    start_index = ord(one) + 1
    end_index = ord(two)
    result = []
    for char_code in range(start_index, end_index):
        result.append(chr(char_code))
    return result


char_one = input()
char_two = input()
result = find_characters_between(char_one, char_two)
print(*result)
