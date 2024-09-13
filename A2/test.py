from assignment2 import split_and_sort

print("Test Default")
nums = [5, 4, -6, -10]
result = split_and_sort(nums)
# Test Case 1: Mixed Positive and Negative Numbers
print("Test Case 1")
nums = [10, -9, 15, 7, 1, -5, 28]
result = split_and_sort(nums)
# Test Case 2: All Negative Including Zero
print("Test Case 2")
nums = [-1, -20, -3, 0, -6]
result = split_and_sort(nums)
# Test Case 3: All Positive with Duplicates
print("Test Case 3")
nums = [5, 23, 5, 23, 42]
result = split_and_sort(nums)
# Test Case 4: Single Negative Number
print("Test Case 4")
nums = [-2]
result = split_and_sort(nums)
# Test Case 5: Edge Cases with Maximum Limit
print("Test Case 5")
nums = [1, -1, 2, -2, 3, -3, 4, -4, -5, -5,  6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15]
result = split_and_sort(nums)
# Test Case 6: Edge Case with Minimum and Maximum Integers
print("Test Case 6")
nums = [-100, 100, -100, 100, -100, 100]
result = split_and_sort(nums)
