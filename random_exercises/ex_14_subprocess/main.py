import sys

def find_max_sum_of_two(numbers):
    max_one = -1
    max_two = -1
    sum = 0
    for val in numbers:
        if val > max_one:
            max_two = max_one
            max_one = val
    return max_two + max_one


li = [5, 9, 7, 11]

print(find_max_sum_of_two(li))
sys.maxsize()