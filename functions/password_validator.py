def checker(word):
    is_valid = True
    if not 6 <= len(word) <= 10:
        is_valid = False
        print('Password must be between 6 and 10 characters')

    if not word.isalnum():
        is_valid = False
        print('Password must consist only of letters and digits')
    count = 0
    for char in word:
        if char.isdigit():
            count += 1
    if count < 2:
        is_valid = False
        print('Password must have at least 2 digits')
    return is_valid


password = input()
valid_password = checker(password)
if valid_password:
    print('Password is valid')
