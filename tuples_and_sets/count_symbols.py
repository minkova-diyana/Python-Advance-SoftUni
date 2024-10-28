phrase = tuple(input())
unique_char = sorted(set(phrase))
for char in unique_char:
    count = phrase.count(char)
    print(f'{char}: {count} time/s')