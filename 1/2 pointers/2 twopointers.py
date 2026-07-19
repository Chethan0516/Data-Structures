# sum upto to the target
# Sort the number

arr = [1, 2, 3, 4, 6]
target = 5

l, r = 0, len(arr) - 1
while l < r:
    cur = arr[l] + arr[r]
    if cur == target:
        print(arr[l], arr[r])
    elif cur > target:
        r =- 1
    else: l+=1

#-------------------------------

# count of unique elements from the sorted array
# Remove duplicates

def remove_duplicates(arr):
    if not arr:
        return 0
    
    l, r = 0, 1
    while r < len(arr):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]
        r += 1
    return l + 1 

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3]
    res = remove_duplicates(arr)
    print(res) # unique count
    print(arr[:res])  # all removed elements

# ----------------------------------------------

# 2 sum

def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        cur = nums[l] + nums[r]
        if cur == target:
            return (nums[l], nums[r])
        elif cur > target:
            r -= 1
        else:
            l += 1

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

#----------------------------------------------

# 3 sum

def three_sum(arr):
    arr.sort()
    res = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        l, r = i+1, len(arr) - 1
        while l < r:
            cur = arr[i] + arr[l] + arr[r]
            if cur > 0:
                r -= 1
            elif cur < 0: l += 1
            else:
                res.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1

                while l < r and arr[l] == arr[l - 1]:
                    l += 1
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1
    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))


#----------------------------------------------------
# Container with most water

def water(height):
    l, r = 0, len(height) - 1
    max_water = 0
    while l < r:
        width = r - l
        max_height = max(height[l], height[r]) * width
        max_water = max(max_height, max_water)
        if height[l] < height[r]:
            l +=  1
        else:
            r -= 1
    return max_water

if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(water(height))

#------------------------------------------------------

# Valid palindrome

def palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal:Panama"
    print(palindrome(s))


#-------------------------------------------

# Dutch national flag

# for loop

nums = [2, 0, 2, 1, 1, 0]
l = []
d = {0:0, 1:0, 2:0}
for n in nums:
    if n == 0:
        d[0] += 1
    elif n == 1:
        d[1] += 1
    else:
        d[2] += 1

for i in range(d[0]):
    l.append(0)
for i in range(d[1]):
    l.append(1)
for i in range(d[2]):
    l.append(2)
print(l)


# 2 pointers
def dnf(nums):
    l, m, h = 0, 0, len(nums) - 1
    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[m], nums[h] = nums[h], nums[m]
            h -= 1
    return nums

if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(dnf(nums))

#------------------------------------------

# Trapping rain water

# Question

#-------------

