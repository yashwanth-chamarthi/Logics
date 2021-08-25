def primecheck(n):
    r = ''
    if n==2 or n==3:
        r = 'prime'
    elif n==1:
        r='neither prime nor not prime'
    for i in range(2,n):
        if n%i==0:
            r = 'not prime'
            break
        elif n%i!=0:
            r = 'prime'
            break
    return r
            
n = int(input('enter the number: '))
print(primecheck(n))