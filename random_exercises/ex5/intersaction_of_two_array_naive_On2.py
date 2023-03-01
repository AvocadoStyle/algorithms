def intersaction_of_2_array(nums1, nums2):
    nums3 = []

    for i, val1 in enumerate(nums1):
        for j, val2 in enumerate(nums2):
            if val1 == val2:
                nums3.append(val1)
                nums2[j] = -1
                break
    return nums3

print(intersaction_of_2_array([1, 2, 2, 1], [2, 2]))