def fibo(n):
    if n == 0:
        return 0
    m = 1
    last1 = 0
    last2 = 0
    n -= 1
    while n > 0:
        last1 = m
        m = last1+last2
        last2 = last1
        n -= 1
    return m

print(fibo(10))