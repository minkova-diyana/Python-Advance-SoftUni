def palindrome_checker(list_numbers):
    it_is_palindrome = False
    for number in list_numbers:
        if number == number[::-1]:
            it_is_palindrome = True
        else:
            it_is_palindrome = False
        print(it_is_palindrome)


given_numbers = input().split(', ')

palindrome_checker(given_numbers)

