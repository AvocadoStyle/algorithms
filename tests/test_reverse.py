def reverse_string(s):
    s = s.split('')
    r = len(s)-1
    l = 0

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)


x = 123
y = str(x)
print(int(reverse_string(y)))
