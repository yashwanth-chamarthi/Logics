def palindrome_check(string):
    x = ''
    for a in string.lower():
        if a.isalpha():
            x += a
    if x==x[::-1]:
        return True
    else:
        return False

string = input()

print(palindrome_check(string))