def plus_one_math(li):
    power = len(li)-1
    number_value = 0
    for v in li:
        number_value += (10**power)*v
        power -= 1
    number_value += 1
    print(number_value)

    if number_value // 10**len(li) > 0:
        power = len(li)
    else:
        power = len(li) - 1
    li[:] = []
    # for val in range(number_value, 0, number_value/(10**power)):
    #     li.append(val)
    while power >= 0:
        val = number_value//(10**power)
        li.append(val)
        number_value -= val*(10**power)
        power -= 1
    return li


li1 = [9, 9, 9]
plus_one_math(li1)
print(li1)