# pythonic solution
def rotate_list(li, k):
    n = len(li)
    k = k % n

    li[:] = li[n-k:] + li[:n-k]

# not pythonic solution
def rotate_list_non_pythonic(li, k):
    n = len(li)
    k = k % n

    p1 = 0

    # for i in range(0,)




li1 = [2, 10, 3, 8, 5]

rotate_list(li1, 2)

print(li1)