def rotate_image(nums):
    n = len(nums)-1
    m = len(nums[0])-1
    left = 0
    right = m
    top = 0
    bot = n
    while left < right:
        for i in range(0, n):
            temp_right = nums[i+left][n-left]
            nums[i+left][n-left] = nums[left][i+left]
            temp_bot = nums[n-left][n-left-i]
            nums[n-left][n-left-i] = temp_right
            temp_left = nums[n-left-i][i+left]
            nums[n-left-i][i+left] = temp_bot
            nums[left][i+left] = temp_left
        left += 1
        right -= 1
        top += 1
        bot -= 1
    return nums




li_simple = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

li_complex = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_image(li_complex))