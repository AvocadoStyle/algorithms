def move_zeros(nums):
    p1 = 0
    for p2 in range(0, len(nums)):
        if nums[p1] == 0 and nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
        if nums[p1] != 0:
            p1 += 1

li = [1, 0]
move_zeros(li)
print(li)