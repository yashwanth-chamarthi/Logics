def fibon(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        print(a)
        a,b = b,a 
        b += a
        
n = int(input())
fibon(n)