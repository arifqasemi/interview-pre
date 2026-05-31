

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

# PATTERN 2: Remove duplicates in-place
def remove_duplicates(arr):
    left = 0  # Write pointer
    for right in range(1, len(arr)):  # Read pointer
        if arr[right] != arr[right - 1]:
            left += 1
            arr[left] = arr[right]
    print(arr)
    return left + 1
nums = [0,0,1,1,1,2,2,3,3,4]
# print(remove_duplicates(nums))
# # PATTERN 3: Container with most water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, area)
        # Move the shorter pointer (to look for taller)
        print(heights[left],heights[right])
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))

## The Core Idea:
## The two-pointer algorithm works best when you have a 
# problem where you need to track two positions simultaneously
#  and their relationship to each other matters for solving the problem.

## Strong hints:
## 
## pair
## subarray
## substring
## palindrome
## left/right
## container
## sorted
## consecutive
## continuous
## range/window

# def reverse_string(s):
#     s = list(s)
#     l,r = 0,len(s)-1
#     while l < r:
#         tmp = s[l]
#         s[l] = s[r]
#         s[r] = tmp
#         l +=1
#         r -=1
#     print(''.join(s))
# reverse_string('hello world')