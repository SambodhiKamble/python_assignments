def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        print(True)

    else:
        print(False)

is_palindrome(1238)
is_palindrome(121)