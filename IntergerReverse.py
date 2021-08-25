def int_rev(num):  
    num=int(str(num)[::-1])  # converting the number to string to reverse "easiest way in python" 
    return num

def int_rev_2(num):
    rev_num=0
    for n in range(len(str(num)),0,-1):
        rev_num+=(num%10)*(10**(n-1))
        num=num//10
    return rev_num

num = int(input('enter the number :'))

print(int_rev(num))

print(int_rev_2(num))