def reverse_int(x):

    sum = 0
    minus_flag = 0
    if x < 0:
        minus_flag = 1
        x = x * -1
    if x >= (2 ** 31 - 1) or x <= -(2 ** 31):
        return 0
    while x > 0:
        num = x % 10
        x = x // 10
        sum = (sum + num) * 10

    sum = sum // 10
    if minus_flag:
         sum = sum * -1
    if sum >= (2 ** 31 - 1) or sum <= -(2 ** 31):
        return 0
    return sum






print(reverse_int(-2147483412))