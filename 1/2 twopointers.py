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