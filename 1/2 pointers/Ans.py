# Task: Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once. 
# Maintain the relative order. Return the number of unique elements.
# Constraint: You must do this by modifying the input array in-place with O(1) extra memory.
# Example:Input:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

l, r = 0, 1
while r < len(nums):
    if nums[l] != nums[r]:
        l += 1
        nums[l] = nums[r]
    r += 1
print(l+1)
print(nums[:l+1])

#--------------------------------------------