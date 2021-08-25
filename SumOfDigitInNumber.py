# Method 1
def sum_of_digit(n):
    res=0
    for i in str(n): # int converted to str because int is not iterable
        res+=int(i)
    return res

# Method 2
def sum_of_digit_2(n):
    res=0
    while n>0:
        res+=n%10
        n=n//10
    return res

n=int(input())

print(sum_of_digit(n))
print(sum_of_digit_2(n))