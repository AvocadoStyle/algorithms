def exchange_math(a, b):
    print(f'a={a} b={b}')
    a = a+b
    b = abs(a-b)
    a = abs(b-a)
    print(f'new: a={a}, b={b}')


exchange_math(100, 150)