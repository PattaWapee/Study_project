def factorial(n):
    fac_n=n
    for i in range(1,n):
        fac_n = fac_n*i
    return fac_n

def recur_factorial(n):
    if n ==1:
        return 1
    else:
        temp = recur_factorial(n-1)
        temp = temp*n
    return temp

print(factorial(5))
print(recur_factorial(5))