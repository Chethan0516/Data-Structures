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

# Scenario: You are designing custom fuel tank geometries optimized for volume containment within rigid structural bounds.
# Task: Given an integer array height of length n, where each element represents a vertical line height at coordinate i. 
# Find two lines that together with the x-axis form a container, such that the container contains the most water. 
# Return the maximum area.Constraint: Time Complexity must be O(N).
# Example:Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]Output: 49

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

l, r = 0, len(height) - 1
cur_water, max_water = 0, 0
while l < r:
    cur_water = min(height[l], height[r]) * (r - l)
    max_water = max(cur_water, max_water)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(max_water)

#-------------------------------------------------------

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 

l, r = 0, len(height) - 1
left_max, right_max = height[l], height[r]
water = 0

while l < r:
    if left_max < right_max:
        l += 1
        left_max = max(left_max, height[l])
        water += left_max - height[l]
    else:
        r -= 1
        right_max = max(right_max, height[r])
        water += right_max - height[r]
print(water)


#-----------------------------------------------------

