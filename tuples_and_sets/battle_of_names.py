rows = int(input())
odd = set()
even = set()
for row in range(1, rows +1):
    ascii_name_sum = sum([ord(char) for char in input()]) // row
    if ascii_name_sum % 2:
        odd.add(ascii_name_sum)
    else:
        even.add(ascii_name_sum)
odd_sums = sum(odd)
even_sums = sum(even)

if odd_sums == even_sums:
    print(*odd|even, sep=', ')
elif odd_sums > even_sums:
    print(*odd-even, sep=', ')
else:
    print(*odd^even, sep=', ')
