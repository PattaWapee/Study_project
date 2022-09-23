def factorial(n):
    fac_n=n
    for i in range(1,n):
        fac_n = fac_n*i
    return fac_n

print(factorial(5))