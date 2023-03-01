def intersaction_of_2_array(nums1, nums2):
    nums3 = []
    nums1.sort()
    nums2.sort()
    len1 = len(nums1)
    len2 = len(nums2)
    p1 = 0
    p2 = 0
    while p1 < len1 and p2 < len2:
        if nums1[p1] == nums2[p2]:
            nums3.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return nums3

print(intersaction_of_2_array([4, 9, 5], [9, 4, 9, 8, 4]))