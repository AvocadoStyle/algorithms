


def two_sum_nlogn(nums, target):
    di = {}
    for i, v in enumerate(nums):
        di[v] = i

    for i, v in enumerate(nums):
        gap = target - v
        if gap in di and di[gap] != i:
            return list((i, di[gap]))



li = [3, 2, 4]
target = 6
print(two_sum_nlogn(li, target))